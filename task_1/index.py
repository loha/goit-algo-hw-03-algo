import os
import shutil
import argparse

def copy_and_sort_files(src_dir, dst_dir):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    try:
        for item in os.listdir(src_dir):
            src_item_path = os.path.join(src_dir, item)
            
            if os.path.isdir(src_item_path):
                # Рекурсивний виклик для директорій
                copy_and_sort_files(src_item_path, dst_dir)
            else:
                # Обробка файлів
                file_extension = os.path.splitext(item)[1][1:]  # Отримуємо розширення файлу без крапки
                if file_extension:
                    dst_item_dir = os.path.join(dst_dir, file_extension)
                else:
                    dst_item_dir = os.path.join(dst_dir, 'no_extension')
                
                if not os.path.exists(dst_item_dir):
                    os.makedirs(dst_item_dir)
                
                dst_item_path = os.path.join(dst_item_dir, item)
                
                # Копіюємо файл до відповідної піддиректорії
                shutil.copy2(src_item_path, dst_item_path)
                print(f'Копіювання файлу {src_item_path} до {dst_item_path}')
    
    except Exception as e:
        print(f'Помилка: {e}')

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням.')
    parser.add_argument('src_dir', help='Шлях до вихідної директорії')
    parser.add_argument('dst_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням: dist)')
    
    args = parser.parse_args()
    
    src_dir = args.src_dir
    dst_dir = args.dst_dir
    
    if not os.path.exists(src_dir):
        print(f'Вихідна директорія {src_dir} не існує.')
        return
    
    copy_and_sort_files(src_dir, dst_dir)

if __name__ == '__main__':
    main()
