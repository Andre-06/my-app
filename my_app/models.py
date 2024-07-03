class Character:
    filename = "my_app/tables/characters.csv"

    def __init__(self, id_character: int, name: str, ability: int, life: int, classes: str) -> None:
        self.id_character = id_character or 0
        self.name = name
        self.ability = ability
        self.life = life
        self.classes = classes

    def save(self) -> int:
        if self.id_character == 0:
            with open(self.filename, "a") as file:
                objects = self.objects()
                id_character = 1 if not objects else objects[-1].id_character + 1
                self.id_character = id_character
                file.write(str(self))
        else:
            with open(self.filename, "r+") as file:
                readline = file.readlines()
                new_lines = [str(self) if line.startswith(str(self.id_character)) else line for line in readline]
                file.seek(0)
                file.writelines(new_lines)
                file.truncate()

        return self.id_character

    @staticmethod
    def objects() -> list:
        with open("my_app/tables/characters.csv", "r") as file:
            list_characters = []
            for line in file:
                id_character, name, ability, life, classes = line.strip().split(",")
                character = Character(int(id_character), name, int(ability), int(life), classes)
                list_characters.append(character)
            return list_characters

    @staticmethod
    def exclude(id_character):
        with open("my_app/tables/characters.csv", "r+") as file:
            readline = file.readlines()
            new_lines = [line for line in readline if not line.startswith(id_character)]
            file.seek(0)
            file.writelines(new_lines)
            file.truncate()

    def __str__(self):
        return ",".join(map(str, [self.id_character, self.name, self.ability, self.life, self.classes])) + "\n"


class Item:
    filename = "my_app/tables/items.csv"

    def __init__(self, id_item: int, character_id: int, name: str, damage: str, critic: str, description: str) -> None:
        self.id_item = id_item or 0
        self.character_id = character_id
        self.name = name
        self.damage = damage
        self.critic = critic
        self.description = description
        

    def save(self) -> int:
        if self.id_item == 0:
            with open(self.filename, "a") as file:
                objects = self.objects()
                id_item = 1 if not objects else objects[-1].id_item + 1
                self.id_item = id_item
                file.write(str(self))
        else:
            with open(self.filename, "r+") as file:
                readline = file.readlines()
                new_lines = [str(self) if line.startswith(str(self.id_item)) else line for line in readline]
                file.seek(0)
                file.writelines(new_lines)
                file.truncate()

        return self.id_item

    @staticmethod
    def objects() -> list:
        with open("my_app/tables/items.csv", "r") as file:
            list_items = []
            for line in file:
                id_item, character_id, name, damage, critic, description = line.strip().split(",")
                item = Item(int(id_item), int(character_id), name, damage, critic, description.replace("/C59878", ","))
                list_items.append(item)
            return list_items

    @staticmethod
    def exclude(id_item):
        with open("my_app/tables/items.csv", "r+") as file:
            readline = file.readlines()
            new_lines = [line for line in readline if not line.startswith(id_item)]
            file.seek(0)
            file.writelines(new_lines)
            file.truncate()

    def __str__(self):
        self.description = self.description.replace(",", "/C59878")
        return ",".join(map(str, [self.id_item, self.character_id, self.name, self.damage, self.critic, self.description])) + "\n"
