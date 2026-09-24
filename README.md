# Cancer Insights — Big Data Analytics on Hadoop (Ambari Sandbox)

A group Big Data course project (DS8003, Toronto Metropolitan University) that builds an end-to-end Hadoop-ecosystem pipeline — ingestion, storage, cleaning, exploratory analysis, and dashboarding — over a global cancer dataset to surface insights on cancer incidence, mortality, and geographic distribution of treatment centers.

## Team (Group 11)
- Devanshu Prajapati
- Nishi Patel
- Avikumar Patel

## Project Definition
Cancer research involves understanding how cancer types relate to patient demographics, disease stage, and treatment outcomes. With dozens of cancer types spread across tissues, geographies, and healthcare systems, it's hard to identify which cancers drive the most cases and deaths, how cancer spreads across tissues, and where care infrastructure is lacking. This project builds a pipeline to clean, explore, and visualize a large cancer dataset to surface those patterns.

## Dataset
- **Source:** [Cancer Database](https://www.kaggle.com/datasets/sujaykapadnis/cancer-database) by Sujay Kapadnis (Kaggle)
- **Format:** CSV, ~470 KB, 1,453 records, 96 attributes
- Covers cancer types, NCI-designated cancer centers, geographic location, OncoTree taxonomy, affected tissue, and U.S. cancer incidence/mortality statistics (`uscsCasesPerYear`, `uscsDeathsPerYear`, etc.)

## Tech Stack (Hortonworks / Ambari Sandbox)
This project was built and run entirely on the **Ambari sandbox** (Hortonworks Data Platform), using the web UIs of the tools below rather than standalone scripts — which is why this repo is primarily documentation, screenshots, and outputs rather than a runnable codebase.

| Tool | Role |
|---|---|
| **Apache NiFi** | Ingested the raw dataset from source and moved it into HDFS |
| **HDFS** | Distributed storage for raw and cleaned datasets |
| **Apache Hive** | SQL-based data cleaning, transformation, and preprocessing |
| **Apache Pig** | Procedural batch transformations and exploratory data analysis |
| **Apache Spark** | In-memory computation for EDA, aggregation, and summary statistics |
| **Tableau** | Interactive charts during exploratory analysis |
| **Power BI** | Final interactive dashboards and heatmaps |

## Pipeline Phases
1. **Ingestion & Storage** — NiFi flow into HDFS (`screenshots/phase1-nifi-hdfs`)
2. **Cleaning & Preprocessing** — Hive queries (`screenshots/phase2-hive`)
3. **Exploratory Data Analysis** — Pig scripts (`screenshots/phase3-pig`)
4. **Aggregation & Feature Summaries** — Spark jobs (`screenshots/phase4-spark`)
5. **Visualization & Dashboards** — Tableau + Power BI (`screenshots/phase5-dashboards`, `screenshots/tableau`)

A local Python script (`scripts/cancer_clean_fixed.py`) was also used to strip stray newline/carriage-return characters from the raw CSV before it was loaded into HDFS, producing `data/cancer_clean_fixed.csv`.

## Key Insights
1. **Top cancers by annual cases** — Breast, lung, prostate, and colorectal cancers together account for more than half of all reported U.S. cancer cases.
2. **Highest-volume cancers** — Non-Hodgkin Lymphoma (~72K cases/year), Leukemia (~51K), and Oral Cancer (~48K) top the volume rankings.
3. **Top 10 deadliest cancers** — Lung cancer leads with ~140,000 deaths/year, far above any other type, largely due to late-stage detection.
4. **Mortality share by cancer type** — Pancreatic cancer, mesothelioma, liver, and stomach cancers show disproportionately high mortality rates relative to their case counts.
5. **Geographic distribution of cancer centers** — NCI-designated centers cluster on the East/West coasts and major metros (e.g., La Jolla, Houston, Chicago), leaving central/rural regions underserved.
6. **Cases vs. deaths** — Breast cancer has very high case counts (~260K) but comparatively low deaths (~42K), reflecting effective early detection, while lung and colon cancer show high mortality relative to cases.
7. **Mortality heatmap by tissue** — Pancreas, liver, and GI-tract tissues show the highest mortality; skin, thyroid, and breast tissues show the best survival outcomes.

## Repository Structure
```
├── data/
│   ├── cancer.csv                  # raw dataset (Kaggle)
│   └── cancer_clean_fixed.csv      # cleaned dataset used downstream
├── scripts/
│   └── cancer_clean_fixed.py       # local CSV cleaning script (newline/CR stripping)
├── docs/
│   ├── DS8001_Project_Proposal_Group11.pdf
│   ├── DS8003_Final_Project_Ideas.pdf
│   ├── DS8003_Project_Report.docx
│   ├── Big_Data_Report.pdf
│   ├── Group_11_CancerInsights_Report.pdf
│   └── Cancer_Presentation.pptx
└── screenshots/
    ├── phase1-nifi-hdfs/   # NiFi flow + HDFS ingestion
    ├── phase2-hive/        # Hive cleaning/transformation queries
    ├── phase3-pig/         # Pig EDA scripts and outputs
    ├── phase4-spark/       # Spark aggregation outputs
    ├── phase5-dashboards/  # Final charts + Power BI dashboard
    └── tableau/            # Tableau exploratory charts
```

## Future Work
- Incorporate patient demographics and risk factors (age, gender, lifestyle, genetics) for targeted prevention strategies
- Build predictive ML models for early cancer risk/survival detection
- Use geospatial analysis to plan expansion of cancer care infrastructure into underserved regions
- Integrate genomic and clinical trial data for precision-medicine insights

## References
Sujay Kapadnis. *Cancer Database*. Kaggle. https://www.kaggle.com/datasets/sujaykapadnis/cancer-database
