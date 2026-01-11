import numpy as np

def read_data(file_name):
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            values = line.strip().split(',')
            values = [int(x) for x in values]
            data.append(values)
    return np.array(data)

def show_data_info(arr):
    print("Data:\n", arr)
    print("Shape:", arr.shape)
    print("Type:", arr.dtype)
    print("-"*30)

def indexing_example(arr):
    print("First row:", arr[0])
    print("Element at row 2, column 3:", arr[1][2])
    print("-"*30)

def slicing_example(arr):
    print("First two rows:\n", arr[:2])
    print("First two columns:\n", arr[:, :2])
    print("-"*30)

def math_operations(arr):
    print("Add 2:\n", arr + 2)
    print("Multiply by 2:\n", arr * 2)
    print("Subtract 1:\n", arr - 1)
    print("Divide by 2:\n", arr / 2)
    print("-"*30)

def statistical_operations(arr):
    print("Mean:", np.mean(arr))
    print("Maximum:", np.max(arr))
    print("Minimum:", np.min(arr))
    print("Sum:", np.sum(arr))
    print("-"*30)

def axis_operations(arr):
    print("Column-wise sum:", np.sum(arr, axis=0))
    print("Row-wise sum:", np.sum(arr, axis=1))
    print("-"*30)

def reshaping_example():
    arr = np.array([1,2,3,4,5,6])
    reshaped = arr.reshape(2,3)
    print("Original array:", arr)
    print("Reshaped array:\n", reshaped)
    print("-"*30)

def save_load_example(arr):
    np.save("saved_data.npy", arr)
    loaded = np.load("saved_data.npy")
    print("Loaded array from file:\n", loaded)
    print("-"*30)

def compare_with_list():
    py_list = [1,2,3,4]
    np_array = np.array(py_list)
    print("Python list +2:", [x + 2 for x in py_list])
    print("NumPy array +2:", np_array + 2)
    print("-"*30)

def main():
    data = read_data("data.txt")
    show_data_info(data)
    indexing_example(data)
    slicing_example(data)
    math_operations(data)
    statistical_operations(data)
    axis_operations(data)
    reshaping_example()
    save_load_example(data)
    compare_with_list()

if __name__ == "__main__":
    main()
