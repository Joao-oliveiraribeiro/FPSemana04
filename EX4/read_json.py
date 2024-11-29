import json

def read_json(path):

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(data)
    except Exception:
        print("Ocorreu um erro!")
    finally:
        print("Processo concluído!")

if __name__ == "__main__":
    file_path= input()
    read_json(file_path)