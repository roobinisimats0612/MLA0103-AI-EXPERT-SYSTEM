"""Educational rule-based example; not medical advice."""
def recommend_diet(age, bmi, condition):
    if age < 0 or bmi <= 0:
        return "Enter a valid age and BMI."
    condition = condition.lower().strip()
    if condition in {"diabetes", "diabetic"}:
        return "Discuss a balanced, clinician-approved meal plan with a qualified professional."
    if condition in {"hypertension", "high blood pressure"}:
        return "Discuss sodium intake and a balanced diet with a healthcare professional."
    if bmi < 18.5:
        return "Consider discussing nutrient-dense meals with a qualified dietitian."
    if bmi >= 25:
        return "Consider balanced meals and professional guidance suited to your needs."
    return "Maintain a varied, balanced diet and regular meals."

if __name__ == "__main__":
    try:
        age = int(input("Age: "))
        bmi = float(input("BMI: "))
        condition = input("Health condition (or none): ")
        print(recommend_diet(age, bmi, condition))
    except ValueError:
        print("Please enter valid numeric age and BMI.")
