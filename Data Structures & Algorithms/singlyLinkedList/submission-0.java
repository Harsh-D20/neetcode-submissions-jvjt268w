class LinkedList {

    ArrayList<Integer> list;

    public LinkedList() {
        list = new ArrayList<Integer>();
    }

    public int get(int index) {
        if(index >= list.size()) {
            return -1;
        }
        else return list.get(index);
    }

    public void insertHead(int val) {
        list.add(0, val);
    }

    public void insertTail(int val) {
        list.add(val);
    }

    public boolean remove(int index) {
        if(index >= list.size()) { return false; }
        else {
            list.remove(index);
            return true;
        }
    }

    public ArrayList<Integer> getValues() {
        return list;
    }
}
