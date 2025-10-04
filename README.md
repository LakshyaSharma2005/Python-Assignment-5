⭐ Task-1

🌟 Student Marks Retrieval Program

This is a simple Python program that stores marks of students in a dictionary and allows the user to retrieve them by entering the student’s name.

📌 Features

* Stores student marks in a dictionary.
* Asks the user if they want to retrieve marks.
* Retrieves and displays the marks when the student’s name is entered.
* Handles invalid inputs and errors gracefully.

📝 Code Explanation

1. A dictionary named `dict` is defined with student names as keys and their marks as values.
2. The user is asked whether they want to retrieve marks (`yes/no`).
3. If the answer is `yes`:

   * The program asks for the student’s name.
   * The first letter of the input is capitalized to match dictionary keys.
   * The marks are displayed if the name exists in the dictionary.
4. If the answer is `no`, it prints `"Okay"`.
5. If the user enters something else, it prints `"Answer in yes or no only!"`.
6. A `try-except` block ensures that errors (like wrong names) are caught and displayed with their exception type.

▶️ Example Run

```
Want to retrieve Marks of any student? (yes/no) yes
Enter the student's name : lakshya
Lakshya's marks is 21
```

```
Want to retrieve Marks of any student? (yes/no) no
Okay
```

```
Want to retrieve Marks of any student? (yes/no) yes
Enter the student's name : Rahul
Error: KeyError
```

⭐ Task-2

🌟 List Slicing and Reversing Example

This Python program demonstrates how to **extract** a portion of a list and then **reverse** it using built-in Python functions.



## 📌 Features

* Creates a list of numbers from **1 to 10**.
* Extracts the **first 5 elements** from the list using slicing.
* Reverses the extracted elements using Python’s `reversed()` function.
* Displays the original list, the extracted part, and the reversed extracted list.



📝 Code Explanation

```python
lakshya = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Original list
first = lakshya[0: 5]                      # Extract first 5 elements
reversed = list(reversed(first))           # Reverse the extracted list

print(f"Original list: {lakshya}")
print(f"Extracted first 5 elements: {first}")
print(f"Reversed extracted elements: {reversed}")
```


▶️ Sample Output


Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first 5 elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]


📚 Concepts Used

* List Slicing → `list[start:end]` extracts elements within a range.
* Reversing → `reversed()` is a built-in function to reverse sequences.
* Type Conversion → `list()` is used to convert the reversed object back to a list.


🚀 How to Run

1. Save the code in a file (e.g., `list_reverse.py`).
2. Run in terminal:

   python list_reverse.py
   

