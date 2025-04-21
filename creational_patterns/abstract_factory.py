from abc import ABC, abstractmethod

# === Abstract Products ===
class Button(ABC):
    @abstractmethod
    def draw(self):
        pass

class Label(ABC):
    @abstractmethod
    def display(self):
        pass

# === Concrete Products for Modern UI ===
class ModernButton(Button):
    def draw(self):
        print("[Modern UI] Drawing a sleek modern button.")

class ModernLabel(Label):
    def display(self):
        print("[Modern UI] Displaying a clean modern label.")

# === Concrete Products for Classic UI ===
class ClassicButton(Button):
    def draw(self):
        print("[Classic UI] Drawing a traditional button.")

class ClassicLabel(Label):
    def display(self):
        print("[Classic UI] Displaying a vintage-style label.")

# === Abstract Factory ===
class UILibraryFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_label(self) -> Label:
        pass

# === Concrete Factories ===
class ModernUILibraryFactory(UILibraryFactory):
    def create_button(self) -> Button:
        return ModernButton()

    def create_label(self) -> Label:
        return ModernLabel()

class ClassicUILibraryFactory(UILibraryFactory):
    def create_button(self) -> Button:
        return ClassicButton()

    def create_label(self) -> Label:
        return ClassicLabel()

# === Client Code Example ===
def build_ui(factory: UILibraryFactory):
    button = factory.create_button()
    label = factory.create_label()
    button.draw()
    label.display()

# === Demo Usage ===
if __name__ == "__main__":
    print(">> Modern UI:")
    modern_factory = ModernUILibraryFactory()
    build_ui(modern_factory)

    print("\n>> Classic UI:")
    classic_factory = ClassicUILibraryFactory()
    build_ui(classic_factory)