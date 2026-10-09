"""Synchronize this workspace's agent trees, then compare every file's bytes."""
import argparse
import filecmp
from pathlib import Path
import shutil
import os


def files(root, errors=None):
    errors = errors if errors is not None else []
    res = {}
    def scan_error(error):
        errors.append(f'{root}: {error}')
    for directory, _, names in os.walk(root, onerror=scan_error):
        for name in names:
            p = Path(directory) / name
            if not name.endswith('.tmp') and name != 'needs_update':
                res[p.relative_to(root)] = p
    return res


def sync_agents(workspace, check_only=False):
    workspace=workspace.resolve()
    primary=(workspace/'.agents').resolve()
    secondary=(workspace/'Engine_2/.agents').resolve()
    if not primary.is_relative_to(workspace) or not secondary.is_relative_to(workspace):
        raise ValueError('Agent directories must stay in the named workspace')
    if not primary.is_dir(): raise FileNotFoundError(primary)
    errors=[]
    if check_only and not secondary.is_dir():
        errors.append(f'{secondary}: secondary agent directory missing')
    left,right=files(primary,errors),files(secondary,errors)
    copied=0
    if not check_only:
        for rel in sorted(set(left)|set(right)):
            p1,p2=primary/rel,secondary/rel
            if rel not in left: source,destination=p2,p1
            elif rel not in right: source,destination=p1,p2
            else:
                try:
                    if filecmp.cmp(p1,p2,shallow=False): continue
                    if p2.stat().st_mtime>p1.stat().st_mtime: source,destination=p2,p1
                    else: source,destination=p1,p2
                except OSError as error:
                    errors.append(f'{rel}: comparison failed: {error}')
                    continue
            if not destination.resolve().is_relative_to(workspace): raise ValueError('Sync destination escaped workspace')
            destination.parent.mkdir(parents=True,exist_ok=True)
            try:
                shutil.copy2(source,destination); copied+=1
            except OSError as error:
                errors.append(f'{rel}: copy failed: {error}')
    left,right=files(primary,errors),files(secondary,errors)
    def safe_cmp(f1, f2):
        try:
            return filecmp.cmp(f1, f2, shallow=False)
        except OSError as error:
            errors.append(f'{f1}: comparison failed: {error}')
            return False
    mismatches=[str(rel) for rel in set(left)|set(right) if rel not in left or rel not in right or not safe_cmp(left[rel],right[rel])]
    print({'primary':str(primary),'secondary':str(secondary),'files_primary':len(left),'files_secondary':len(right),'copied':copied,'byte_mismatches':len(mismatches),'examples':mismatches[:10],'errors':errors[:10],'error_count':len(errors)})
    return not mismatches and not errors


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--check-only',action='store_true')
    args=parser.parse_args()
    raise SystemExit(0 if sync_agents(args.root,args.check_only) else 1)
