class DynamicArray {

    private int[] elems;
    private int capacity;
    private int size;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        elems = new int[capacity];
        size = 0;
    }

    public int get(int i) {
        return elems[i];
    }

    public void set(int i, int n) {
        elems[i] = n;
    }

    public void pushback(int n) {
        if(size + 1 > capacity) {
            resize();
        }
        elems[size] = n;
        size++;
    }

    public int popback() {
        size--;
        return elems[size];
    }

    private void resize() {
        int new_capacity = capacity * 2;
        int[] temp = new int[new_capacity];
        for(int i=0; i < size; i++) {
            temp[i] = elems[i];
        }
        elems = temp;
        capacity = new_capacity;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
