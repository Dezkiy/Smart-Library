
C4Context
    title Smart Library System - System Context Diagram

    Person(member, "Library Member", "A person who borrows books and accesses library resources")
    System(librarySystem, "Smart Library System", "Manages library resources and member interactions")
    System_Ext(database, "Library Database", "Stores library data", $sprite="Database")
    System_Ext(digitalContent, "Digital Content Storage", "Stores digital resources", $sprite="Cloud")

    Rel(member, librarySystem, "Uses", "Uses")
    Rel(librarySystem, database, "Stores and retrieves data", "Stores & Retrieves")
    Rel(librarySystem, digitalContent, "Stores and retrieves digital content", "Stores & Retrieves")

    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="3")
    ' Styling
    skinparam {
        shadowing false
        defaultTextAlignment center
        component {
            BackgroundColor LightBlue
            BorderColor DarkBlue
        }
        database {
            BackgroundColor LightYellow
            BorderColor Orange
        }
        cloud {
            BackgroundColor LightGreen
            BorderColor DarkGreen
        }
        person {
            BackgroundColor LightGray
            BorderColor Black
        }
        rectangle {
            BackgroundColor White
            BorderColor Gray
        }
        ArrowColor DarkSlateGray
    }
