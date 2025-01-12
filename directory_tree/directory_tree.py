# mostra uma arvore de diretorios e arquivos
import os

def directory_tree(path):
    print(f'+ {path}')

    if os.path.isdir(path):
        items = os.listdir(path)
        items.sort()
        for item in items:
            directory_tree(os.path.join(path, item))

def main():
    path = input("Enter the path: ")
    try:
        directory_tree(path)
    except Exception as e:
        print("Error: ", str(e))

if __name__ == '__main__':
    main()