# FAIDM Group Project - Task Summary
## Your Work Until Tuesday 11am Meeting

---

### Dataset Files Required

Place all these files in the same directory as the notebook:

| File | Status | Notes |
|------|--------|-------|
| studentInfo.csv | ✓ Have | Demographics + final_result (target) |
| studentAssessment.csv | ✓ Have | Assessment submissions |
| assessments.csv | ✓ Have | Assessment metadata |
| courses.csv | ✓ Have | Module info |
| studentRegistration.csv | ✓ Have | Registration dates |
| vle.csv | ✓ Have | VLE resource metadata |
| **studentVle.csv** | ✓ Confirmed | VLE click data (you have this!) |

---

### Your Two Tasks

#### Task 1: Predictive Model (Supervised ML)
**Objective:** Predict Pass/Distinction vs Fail/Withdrawn

**What the notebook does:**
- Merges all 7 datasets into unified student-level data
- Creates 40+ features:
  - Demographics (encoded)
  - Assessment performance (avg, min, max, by type)
  - Submission timeliness (days early/late)
  - VLE engagement (total clicks, active days, resources)
  - Early indicators (first 2 weeks, pre-course clicks)
  - Activity-type clicks (oucontent, resource, quiz, etc.)
- Trains 3 models: Logistic Regression, Random Forest, Gradient Boosting
- Hyperparameter tuning with GridSearchCV
- Feature importance analysis

**For Tuesday, note:**
- [ ] Which model performs best (likely RF based on AUC-ROC)
- [ ] Top 5 most important features
- [ ] Any surprising results

---

#### Task 2: Clustering Model (Unsupervised ML)
**Objective:** Segment students by engagement patterns

**What the notebook does:**
- K-Means clustering on engagement features
- Evaluates k=2 to 10 using Elbow, Silhouette, Davies-Bouldin
- Profiles clusters by mean feature values
- Maps clusters to final outcomes

**For Tuesday, interpret:**
- [ ] What does each cluster represent? (e.g., "High engagers", "Late starters")
- [ ] Which cluster has highest failure rate?
- [ ] What intervention would you recommend per cluster?

---

### Feature Engineering Summary

The notebook creates these feature groups:

**Registration Features:**
- `registered_early` - Boolean: registered before course start
- `days_before_start` - Days registered before day 0

**Assessment Features:**
- `avg_score`, `score_std`, `min_score`, `max_score`
- `num_assessments_submitted`
- `avg_days_early`, `worst_days_early` - Submission timeliness
- `tma_avg_score`, `cma_avg_score`, `exam_avg_score` - By type

**VLE Engagement Features:**
- `total_clicks`, `avg_daily_clicks`, `max_daily_clicks`
- `active_days`, `unique_resources`
- `engagement_span` - First to last access
- `clicks_per_active_day`
- `clicks_oucontent`, `clicks_resource`, `clicks_quiz`, etc. - By activity type

**Early Indicators (key for intervention!):**
- `early_clicks`, `early_active_days`, `early_resources` - First 2 weeks
- `pre_course_clicks` - Activity before day 0

---

### CRISP-DM Coverage

| Phase | Status | Notes |
|-------|--------|-------|
| 1. Business Understanding | ✅ | Problem defined, success criteria set |
| 2. Data Understanding | ✅ | EDA, missing values, distributions |
| 3. Data Preparation | ✅ | Feature engineering, encoding, merging |
| 4. Modelling | ✅ | 3 classifiers + K-Means + tuning |
| 5. Evaluation | ✅ | Metrics, confusion matrix, feature importance |
| 6. Deployment | 📝 | Considerations documented |

---

### How to Run

1. Put all 7 CSV files in a folder
2. Open `FAIDM_Project_Work.ipynb` in Jupyter
3. Update `DATA_PATH` if needed (line 2 of data loading cell)
4. Run all cells (Kernel → Restart & Run All)
5. Takes ~5-10 minutes depending on your machine

---

### Key Presentation Points for Tuesday

When comparing with your group:

1. **Feature Engineering:** What features did each person create?
2. **Model Selection:** Which model worked best? Why?
3. **Feature Importance:** What predicts success/failure?
4. **Clusters:** How many? What do they mean?
5. **Early Warning:** Can we predict at-risk students in week 2?
6. **Recommendations:** What would you tell the university?

---

### Questions for Amir

1. Can we use statistical methods (Pearson correlation) beyond module content?
2. Does everyone need to present the slides?

---

**Deadline Reminder:** Presentation W/C 26th January 2026 (15 min + 5 min Q&A)
