from typing import List # Standard practice for list typing

class Student:
    # 1. Type Hints added to arguments
    def __init__(self, name: str, student_id: int, grades: List[int]):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    # 2. Return type hint added (-> float)
    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0  # Return float for consistency
        return sum(self.grades) / len(self.grades)

    # 3. Return type hint added (-> bool)
    def is_passing(self) -> bool:
        return self.calculate_average() >= 60.0

    def __str__(self) -> str:
        return f"{self.name} ({self.student_id}) - Grades: {self.grades}"

# 4. The Entry Point Guard
if __name__ == "__main__":
    student1 = Student("John", 1, [80, 90, 70])
    student2 = Student("Jane", 2, [])

    # Using f-strings for the report (Cleaner output)
    print(f"Student: {student1.name}, Avg: {student1.calculate_average():.2f}, Pass: {student1.is_passing()}")
    print(f"Student: {student2.name}, Avg: {student2.calculate_average():.2f}, Pass: {student2.is_passing()}")