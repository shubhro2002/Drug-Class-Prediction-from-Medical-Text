# Drug-Class-Prediction-from-Medical-Text

The primary goal of this project is to build an automated system capable of predicting the correct drug class(es) based on descriptive metadata.
Since many drugs belong to multiple therapeutic classes, the problem is framed as a multi-label text classification task.

This system can be extended into:

- Clinical decision support

- Drug categorization

- Drug recommendation engines

- Medical text mining applications

## Dataset

The dataset contains drug information with multiple key textual fields such as:

| Column Name                     | Description                         |
| ------------------------------- | ----------------------------------- |
| `generic_name`                  | Official generic name of the drug   |
| `brand_names`                   | Marketed brand names                |
| `medical_condition`             | Condition(s) treated by the drug    |
| `side_effects`                  | Common adverse effects              |
| `medical_condition_description` | Description of the target condition |
| `drug_classes`                  | **Target labels** (multi-label)     |

### Target Variable

`drug_classes` is multi-label in nature, meaning a single drug may belong to multiple therapeutic categories.

## Data Pre-Processing

Multiple preprocessing steps were performed to clean, merge, structure, and prepare the textual data.

✔ Text Cleaning

- Lowercasing

- Removing punctuation

- Removing special characters and numbers

- Removing URLs and extra whitespace

- Expanding contractions (if present)

- Normalizing drug names

✔ Missing Value Handling

- Filled missing text fields with `unknown`

- Removed rows with missing target labels

✔ Text Merging

- A unified text feature was constructed by combining:

`generic_name + " " + brand_names + " " +
medical_condition + " " + side_effects + " " +
medical_condition_description`

This enriched text representation improves model context.

✔ Label Preprocessing

- Multi-label binarization (One-vs-Rest format)

- Mapping strings → list of classes

- Creating a multi-hot encoded target matrix

## Exploratory Data Analysis (EDA)

Comprehensive EDA was performed to understand the dataset distribution.

### EDA Highlights

- Label Distribution

- Text Analysis

- Multi-Label Structure

## Modeling Approach

**Problem Type**: Multi-label text classification

**Feature Extraction**: TF-IDF Vectorization

**Model**: Linear SVM (One-vs-Rest)

## Model Evaluation

Evaluation Metrics (Multi-Label Specific)

- Micro F1-score

- Macro F1-score

- Hamming Loss

- Jaccard Similarity Score

- Precision & Recall

Evaluation was performed on a train–test split (75-25).

## Future Improvements

- Use BioBERT, SciBERT, or ClinicalBERT embeddings.

- Implement Transformer-based multi-label classifiers.

- Apply SMOTE or label-specific oversampling to reduce imbalance.

- Integrate with a drug recommendation system.

- Deploy the model as an API for real-time classification.
