## 🧠 Creational Patterns Justification

This project applies six creational design patterns to model components of a Library Management System. Each pattern is carefully chosen based on its strengths in solving specific object-creation problems.

### 1. 🏭 Simple Factory

**Purpose**: Centralizes object creation for book types without exposing instantiation logic.

**Use Case**: Used to return different types of `Book` objects based on genre or category.

**Justification**:
- Reduces coupling between object creation and usage.
- Simplifies instantiation logic in the client code.
- Encourages code reuse and scalability.

---

### 2. 🧱 Factory Method

**Purpose**: Allows subclasses to decide which object to instantiate.

**Use Case**: Used for sending notifications through different channels (e.g., email, SMS) by implementing `Notifier` subclasses like `EmailNotifier` and `SMSNotifier`.

**Justification**:
- Adheres to the Open/Closed Principle.
- Allows client code to use an interface without knowing the exact class used to instantiate the object.

---

### 3. 🧪 Abstract Factory

**Purpose**: Produces families of related or dependent objects without specifying their concrete classes.

**Use Case**: Helps create consistent sets of related objects like UI components or domain-specific services.

**Justification**:
- Maintains consistency across products from the same factory.
- Makes it easy to switch between object families with minimal code changes.

---

### 4. 🧰 Builder

**Purpose**: Constructs complex objects step-by-step.

**Use Case**: Builds a `Book` object with both required and optional attributes using the `BookBuilder` class.

**Justification**:
- Avoids telescoping constructor anti-pattern.
- Makes object construction more readable and flexible.
- Suitable for immutable objects or when many optional parameters exist.

---

### 5. 🧬 Prototype

**Purpose**: Creates new objects by cloning existing ones.

**Use Case**: Clones a prototype `LibraryMember` and customizes the clone with user-specific details.

**Justification**:
- Efficiently creates new objects that share a common configuration.
- Useful when object creation is expensive or complex.

---

### 6. 🔒 Singleton

**Purpose**: Ensures a class has only one instance and provides a global point of access to it.

**Use Case**: Manages a centralized `LibraryCatalog` where all books are stored and accessed.

**Justification**:
- Guarantees a single, consistent instance of the catalog throughout the application.
- Prevents conflicts or redundancy in accessing or modifying shared data.

---
