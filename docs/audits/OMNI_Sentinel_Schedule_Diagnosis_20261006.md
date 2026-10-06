# Sentinel schedule correction — 2026-10-06

The user requires automatic reviews only at UTC minutes 14, 29, 44 and 59. Automatic heartbeats arrived at 07:41 and 07:46 UTC instead. The 07:46 audit was interrupted by the user's correction; no additional debate was launched for that off-cadence cycle.

The installed desktop app source contains two relevant scheduling behaviors:

- In bootstrap-BXPOZU-a.js, the recurring-run calculation adds a deterministic random delay from 0 to 119 seconds to hourly, daily and weekly recurrence types. This applies to the previously configured hourly schedule.
- In main-B5_S2vFm.js, a heartbeat whose chat is busy is deferred and retried later. The retry can occur outside the original requested minute.

These findings come from read-only inspection of the installed app.asar in OpenAI.Codex_26.930.4958.0. No installed application file or scheduler database was modified directly.

The existing omni-mt5-sentinel heartbeat was paused through the automation tool. Its recurrence was changed, while paused, to a minute-filtered wall-clock rule that selects only minutes 14, 29, 44 and 59 and avoids the installed app's hourly jitter path. The prompt now requires silent skipping of delayed or off-cadence automatic cycles before commentary, account tools or agent launches.

Eight consecutive occurrences were independently checked with the recurrence parser: 07:59, 08:14, 08:29, 08:44, 08:59, 09:14, 09:29 and 09:44 UTC. This proves the selected recurrence times; it does not eliminate the app's busy-chat deferral behavior or prove delivery timing.

An independent scheduled job would avoid dependence on this chat becoming idle. The user was asked to choose between that separate-task execution model and leaving the heartbeat paused. No replacement job was created without that choice. The proposed independent job would retain the minute-filtered recurrence, strict start-time guard, existing account-bound protective enforcement, multi-agent review and repository evidence workflow.

The execution daemon was not restarted, stopped or reconfigured by this correction. Its native inventory protection and order-dispatch cadence are independent of the Sentinel automation.
