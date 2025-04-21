from creational_patterns.abstract_factory import (
    ModernUILibraryFactory,
    ClassicUILibraryFactory,
    Button,
    Label,
)


def test_modern_ui_factory_creation():
    modern_factory = ModernUILibraryFactory()
    assert isinstance(modern_factory, ModernUILibraryFactory)


def test_classic_ui_factory_creation():
    classic_factory = ClassicUILibraryFactory()
    assert isinstance(classic_factory, ClassicUILibraryFactory)


def test_modern_ui_factory_creates_button():
    modern_factory = ModernUILibraryFactory()
    button = modern_factory.create_button()
    assert isinstance(button, Button)


def test_modern_ui_factory_creates_label():
    modern_factory = ModernUILibraryFactory()
    label = modern_factory.create_label()
    assert isinstance(label, Label)


def test_classic_ui_factory_creates_button():
    classic_factory = ClassicUILibraryFactory()
    button = classic_factory.create_button()
    assert isinstance(button, Button)


def test_classic_ui_factory_creates_label():
    classic_factory = ClassicUILibraryFactory()
    label = classic_factory.create_label()
    assert isinstance(label, Label)

