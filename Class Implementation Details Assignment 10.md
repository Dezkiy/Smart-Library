# Assignment 10:

## Language Choice

Python was chosen for this project due to its:

* Readability and ease of use, which facilitates rapid development.
* Strong support for object-oriented programming.
* Extensive standard library.

## Key Design Decisions

* **Protected Attributes:** Attributes are prefixed with an underscore (e.g., `_title`) to indicate they are intended for internal use within the class.
* **Getters and Setters:** Getters (e.g., `get_title()`) are provided to access attribute values, and setters (e.g., `set_available_copies()`) are used to modify attributes when necessary, to control access and potential validation.
* **Creational Patterns:** Design patterns like Factory Method, Builder, Prototype, and Singleton are used to manage object creation in a flexible and maintainable way.
* **Associations:** Classes like `Loan` and `Reservation` maintain associations with `Book` and `LibraryMember` to model relationships between entities.
* **Error Handling:** Exceptions (e.g., `ValueError`) are used to handle invalid input or operations.
* **Type Hinting:** Type hints are used to improve code readability and maintainability.
