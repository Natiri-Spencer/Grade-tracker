import io
import csv
import json
#Csv data
csv_data="""name,score1,score2,score3,score4,score5
Queenter Naliaka,67,76,bad data,53,80
Cyprian Juma,67,36,67,48,75
Agneta Muchele,45,46,67,49
Hudson wawire,90,88,87,90,85
Fatuma Nasuo,78,56,89,47,50
Angel Khafumi,90,56,89,66"""

#functions
def parse_score(value):
     try:
          return int(value)
     except(ValueError,TypeError):
          return None

def calculate_avg(scores):
     valid = [s for s in scores if s is not None]
     if not valid:
          return None
     return round(sum(valid)/len(valid),1)
#CBC grading
def grade_learner(avg):
     if avg is None:return "N/A"
     if avg >= 90:return "EE1"
     elif avg >= 77:return "EE2"
     elif avg >= 60:return "ME1"
     elif avg >= 48:return "ME2"
     elif avg >= 34:return "AE1"
     elif avg >= 26:return "AE2"
     elif avg >= 16:return "BE1"
     else:return "BE2"
#Process CSv
f = io.StringIO(csv_data)
reader = csv.DictReader(f)
results = []
print(f"{'='* 50} ")
print(f"{'NAME':<20} {'AVG':>5} {'GRADE':>5} NOTES")
print(f"{'='*50}")
for row in reader:
     scores = [
          parse_score(row["score1"]),
          parse_score(row["score2"]),
          parse_score(row["score3"]),
          parse_score(row["score3"]),
          parse_score(row["score4"]),
          parse_score(row["score5"])
     ]
     invalid_count = scores.count(None)
     avg = calculate_avg(scores)
     grade = grade_learner(avg)
     notes = f"{invalid_count} invalid score(s)" if invalid_count else "All scores valid"
     print(f"{row['name']:<20} {str(avg):>5} {grade:>5} {notes}")

     results.append({
          "name":row["name"],
          "scores": [row["score1"], row["score2"], row["score3"], row["score4"], row["score5"]],
          "average": avg,
          "grade":grade
          })
     print(f"{'='*50}")

#Class summary
valid_avgs = [r["average"] for r in results if r["average"] is not None]
class_avg = round(sum(valid_avgs)/len(valid_avgs), 1)
print(f"\nClass Average:{class_avg}")
print(f"Student:{len(results)}")
#Export as Json
print("\n Json Export:")
print(json.dumps(results, indent=2))
