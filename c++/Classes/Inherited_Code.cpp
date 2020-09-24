

class BadLengthException{
    private:
        int num;
    public:
        BadLengthException(int n): num(n) {}

        int what()
        {
            return num;
        }
};

