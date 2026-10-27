# 🚀 Ultra Pipeline & Power BI Modernization Plan: Production-Ready Architecture

> **Target Workspace:** `C:\Users\SIGMA\Downloads\Ultra`  
> **ETL & Data Structuring Hub:** `Data - V2\Main_V2.xlsx`  
> **Executive Analytics Dashboard:** `Dashboard - V2\DashboardPET.pbix`  
> **Author/Orchestrator:** Antigravity High-Fidelity Engineering Swarm  
> **Status:** Phase 1 (Planning & Architecture Approval)

---

## 1. Executive Summary & Core Objectives

The `Ultra` ecosystem represents an industrial-grade enterprise analytics pipeline tracking PET polymer operations (Domestic Orders, Export Orders, Sales Targets, Inventory Ageing, Plant Stocks, STO Logistics, Dispatch Tracking, and PTA Material Consumption).

### The Primary Problems Identified
1. **Hardcoded File & Folder Paths**:
   All 26 Power Queries in `Main_V2.xlsx` hardcode paths to `C:\Users\karanbir3.singh\OneDrive - Reliance Corporate IT Park Limited\RIL - GET'23\Stint-4\PET BUSINESS\PET - Power BI\Data - V2\...`. When run on any other user profile, folder, or drive, queries immediately fail with `DataSource.NotFound`.
2. **Missing/Orphaned External Dependencies**:
   `#"MEPL Stock"` queries an external OneDrive workbook `M__L.xlsx` located outside the package, causing refresh failures when executed standalone.
3. **Legacy Dashboard Aesthetics & UX**:
   `DashboardPET.pbix` uses legacy dense tabular grids, non-hierarchical font sizing, plain card visuals, and outdated report themes, missing modern Fluent/Executive visual design, KPI sparklines, executive summary landing pages, and interactive card containers.
4. **Cloud-Tethered Connection Artifacts**:
   `DashboardPET.pbix` contains remote artifact bindings pointing to a cloud tenant dataset (`d98f30ea-8649-40bd-99b5-2da7ee66868d`), which causes connection errors on offline or separate tenant environments.

### Core Objectives
- **Dynamic Path Fetching Everywhere**: Zero hardcoded paths. All queries will dynamically resolve their location relative to the current workbook and folder location automatically.
- **Zero-Error Execution**: Every single query will have defensive error handling (`try ... otherwise`), robust column type conversions, and graceful fallbacks for missing optional feeds.
- **Excel Data Dictionary & Transparency**: Enrich `Main_V2.xlsx` with complete query documentation, descriptions, and a master control sheet.
- **Modern Executive Dashboard**: Modernize `DashboardPET.pbix` with an executive design system, modern card visuals, streamlined KPIs, clean visual padding, and structured analytical navigation.

---

## 2. Architecture & Dynamic Path Resolution Engine

### 2.1 The Two-Tier Dynamic Path Architecture
In order to guarantee that `Main_V2.xlsx` works seamlessly anywhere it is moved:

```
[Main_V2.xlsx Workbook]
         │
         ├── Tier 1 (Automatic Excel Cell Formula)
         │     Sheet: 'Config' | Table: 'tblConfig' | Column: 'BasePath'
         │     Formula: =LEFT(CELL("filename",A1),FIND("[",CELL("filename",A1))-1)
         │     Result: "C:\Users\SIGMA\Downloads\Ultra\Data - V2\" (Auto-updates on file open)
         │
         └── Tier 2 (Power Query Dynamic M Parameter: 'BasePath')
               Evaluates tblConfig -> Falls back to relative current folder -> Fallback default
```

### 2.2 Power Query `BasePath` Implementation
```powerquery
shared BasePath = let
    // 1. Try reading dynamic workbook formula table
    DynamicFromTable = try Text.Trim(Excel.CurrentWorkbook(){[Name="tblConfig"]}[Content]{0}[BasePath]) otherwise null,
    // 2. Try reading dynamic named range
    DynamicFromCell  = try Text.Trim(Excel.CurrentWorkbook(){[Name="BasePath"]}[Content]{0}[Column1]) otherwise null,
    // 3. Fallback to existing active directory if formula uncalculated
    FallbackPath     = "C:\Users\SIGMA\Downloads\Ultra\Data - V2\",
    
    Resolved = if DynamicFromTable <> null and DynamicFromTable <> "" then DynamicFromTable
               else if DynamicFromCell <> null and DynamicFromCell <> "" then DynamicFromCell
               else FallbackPath,
    Normalized = if Text.EndsWith(Resolved, "\") then Resolved else Resolved & "\"
in
    Normalized meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true];
```

---

## 3. Detailed Audit of All 26 Queries in `Main_V2.xlsx`

| # | Query Name | Source Category | Dynamic Path Mapping | Key Transformations & Error Hardening |
|---|------------|-----------------|----------------------|---------------------------------------|
| 01 | `BasePath` | Config Engine | `Excel.CurrentWorkbook()` | Centralized dynamic root directory resolver |
| 02 | `Master Billing` | Folder | `BasePath & "2_Order_Management\Billing"` | Multi-file text ingestion, header trimming, safe numeric casting for `Disp Qty` |
| 03 | `Sample File (2)` | Folder | `BasePath & "2_Order_Management\Billing"` | First binary stream extraction for helper transform |
| 04 | `Parameter2` | Parameter | Binary metadata | Helper parameter query |
| 05 | `Transform Sample File (2)`| Helper | Csv parser | Delimiter `\|`, 21 columns, Latin-1 encoding |
| 06 | `Transform File (2)` | Function | Function invocation | Safe line-by-line transform |
| 07 | `DMD Export Pendo` | File | `BasePath & "3_Sales_Distribution_Management\DH_Export_STO.txt"` | Delimiter `\|`, header promotion, YTTS function trim |
| 08 | `HMD Export Pendo` | File | `BasePath & "3_Sales_Distribution_Management\HZ_Export_STO.txt"` | Delimiter `\|`, 19 columns, empty column strip |
| 09 | `Combined Export Pendo` | Table Combine | Memory (`DMD` + `HMD`) | Union of export pendos, whitespace trimming |
| 10 | `STO` | File | `BasePath & "2_Order_Management\4_STO.txt"` | 54 columns pipe-delimited, filter non-empty doc dates, exclude transit zones `INHZR`/`INJNP` |
| 11 | `Imported PET Production` | File | `BasePath & "4_PTA_Imported\Material Consumption\Imported PET Production.txt"` | 25 columns, header promotion, material consumption filtering |
| 12 | `Domestic Orders Dump` | File | `BasePath & "2_Order_Management\1_Domestic_Order_Dump.txt"` | 26 columns, filter sales types `Z300`, `Z302`, `Z305` |
| 13 | `Domestic Orders Template 2`| File | `BasePath & "2_Order_Management\Domestic_Order_Template.xlsx"` | Excel workbook read, sheet `Domestic Order Template 2`, numeric quantity types |
| 14 | `Domestic Orders` | Table Combine | Memory (`Template 2` + `Dump`) | Master domestic order backlog |
| 15 | `Last Month Sales` | File | `BasePath & "2_Order_Management\2_Last_Month_Sales.txt"` | 26 columns, sales document filtering, numeric delivered/billed quantities |
| 16 | `SecondLast Month Sales` | File | `BasePath & "2_Order_Management\3_SecondLast_Month_Sales.txt"` | CSV comma/pipe hybrid split, filter distribution channel `10`, sales types `Z300`/`Z302`/`Z305` |
| 17 | `MEPL Stock` | External File | `BasePath & "1_Stock_Management\M__L.xlsx"` (Defensive Fallback) | Wrapped in `try ... otherwise` with fallback to cached table schema |
| 18 | `RIL Stock` | File | `BasePath & "1_Stock_Management\Stock.txt"` | Pipe-delimited parsing, column splitting, block/unrestricted metric renames |
| 19 | `All_Site_Stock` | Table Combine | Memory (`RIL Stock` + `MEPL Stock`) | Combined site inventory, filter grades `B80 J` and `B84 J` |
| 20 | `Domestic_Pendo` | File | `BasePath & "3_Sales_Distribution_Management\Domestic_Pending_Shipment.txt"` | Delimited pipeline, header promotion, numeric order/pending quantities |
| 21 | `Domestic_DO_Pendo` | Table Link | `Excel.CurrentWorkbook(){[Name="Domestic_Orders"]}` | Column projection, date typing, delivery order type tagging (`DO`) |
| 22 | `Domestic_STO_Pendo`| Table Link | `Excel.CurrentWorkbook(){[Name="STO"]}` | Column selection, destination mapping, stock transfer type tagging (`STO`) |
| 23 | `Combined_Domestic_Pendo`| Table Combine | Memory (`DO_Pendo` + `STO_Pendo`) | Master unified pending order & shipment schedule |
| 24 | `DomesticSales 2024-2025`| File | `BasePath & "2_Order_Management\5_DomesticSales 2024-2025.txt"` | Historical FY24-25 baseline, sales types `Z300`/`Z302` |
| 25 | `DomesticSales 2023-2024`| File | `BasePath & "2_Order_Management\6_DomesticSales 2023-2024.txt"` | Historical FY23-24 baseline, 26 column structure |
| 26 | `Ageing Analysis 2` | Table Link | `Excel.CurrentWorkbook(){[Name="All_Site_Stock"]}` | Exclusion of pilot plants `39E3`/`39EA`, error row cleansing, ageing brackets |
| 27 | `Current_Month_Export_Billing`| Table Link | `Excel.CurrentWorkbook(){[Name="Master_Billing"]}` | Current month date filter, classification `Export Stuffing` |

---

## 4. Modern Dashboard Transformation Blueprint (`DashboardPET.pbix`)

### 4.1 Visual Hierarchy & Design System (Fluent Analytics Standard)
- **Design Theme**: Corporate Executive Navy & Slate (Hex: `#0F172A` background, `#FFFFFF` visual card containers, `#1E40AF` primary metric, `#059669` positive status, `#DC2626` urgent ageing/block).
- **Grid Structure**: 12-column responsive layout, 16px consistent margin, 8px corner radius on visual cards with 1px border stroke (`#E2E8F0`).
- **Typography**: Segoe UI / Segoe UI Semibold, standard font scale (Title: 18pt bold, Subtitle/Section: 12pt semibold, KPIs: 22-26pt bold tabular figures, Data tables: 9pt regular).

### 4.2 Page Rationalization & Enhancement
The 19 scattered pages will be structured into an intuitive executive workflow:
1. **Executive Command Center (New Page 1)**: High-level cockpit featuring 4 executive KPI cards (Total Stock MT, Pending DO MT, Month-to-Date Billing MT, Total Ageing > 60 Days MT) with month-over-month trajectory badges.
2. **Order Management & Dispatch**: Modernized `Domestic_Orders` & `Dispatch Report` with interactive customer/region slicers, order progress bars, and credit release indicators.
3. **Inventory & Warehouse Health**: Unified `WH Stock` & `Warehouse` page featuring interactive treemap of stock distribution by Plant & Grade, storage location utilization, and blocked stock alerts.
4. **Ageing Risk Forensic Matrix**: Upgraded `Ageing` page replacing raw tables with conditional gradient tables (0-30d, 31-60d, 61-90d, 90d+) and regional drilldown.
5. **Logistics & Pending Shipments**: Upgraded `Logistics` view with delivery block status, truck allocation, and daily dispatch targets.

### 4.3 Data Model & Connection Modernization
- Remove obsolete cloud remote artifact bindings in `Connections` to prevent auth popups.
- Bind the PBIR report directly to local tables exported by `Main_V2.xlsx`.
- Ensure all DAX measures use explicit formatting strings (`#,##0.0 MT`, `₹#,##0.00 Cr`, `0.0%`).

---

## 5. Work Breakdown Structure & Multi-Agent Execution Phases

### Phase 1: Planning & Pre-Flight Review (Current Turn)
- [x] Complete codebase & data pipeline discovery in `C:\Users\SIGMA\Downloads\Ultra`.
- [x] Extract and audit all 26 queries in `Main_V2.xlsx`.
- [x] Audit report definition JSON files and visuals in `DashboardPET.pbix`.
- [x] Generate master modernization specification (`ultra-production-pipeline-modernization.md`).
- [ ] **User Approval Gate**: Await operator confirmation to proceed to Phase 2.

### Phase 2: Implementation (Post-Approval Parallel Swarm)
- **Agent 1 (Data Architect - Excel & Power Query Engine)**:
  * Create `Config` sheet with dynamic Excel formula in `Main_V2.xlsx`.
  * Inject dynamic `BasePath` parameter and update all 15 path references in `Section1.m`.
  * Add defensive error handling for `MEPL Stock` and optional files.
  * Rebuild `customXml/item4.xml` DataMashup package and repackage `Main_V2.xlsx`.
- **Agent 2 (Data Documentation & Data Dictionary Specialist)**:
  * Add a `Data_Dictionary` sheet in `Main_V2.xlsx` describing every table, source, column definition, data type, and business logic.
- **Agent 3 (Power BI & UI/UX Specialist)**:
  * Update `Report/definition/` files in `DashboardPET.pbix` with executive visual containers, modern theme JSON, clean card visuals, and consistent layout.
  * Fix `Connections` bindings to allow seamless offline and dynamic model refresh.
- **Agent 4 (QA & Verification Auditor)**:
  * Run Python verification scripts to test Power Query syntax, package integrity, and zip validity.
  * Certify zero errors across all components.

---

## 6. Verification Criteria & Deliverables
1. **Dynamic Path Test**: Moving the `Ultra` folder to any directory or drive requires zero manual code edits; queries resolve paths automatically.
2. **Excel Refresh Test**: `Main_V2.xlsx` contains valid DataMashup packages and opens without XML or query corruption.
3. **Dashboard Integrity**: `DashboardPET.pbix` report definition passes schema validation with modern styling applied.
4. **Documentation**: Clear in-workbook descriptions and markdown documentation.
