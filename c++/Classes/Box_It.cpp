

class Box{
    int l, b, h;

    public:
    Box() : l(0), b(0), h(0) {}
    Box(int x, int y, int z) : l(x), b(y), h(z) {}
    Box(const Box& B) {
        this->l = B.l;
        this->b = B.b;
        this->h = B.h;
    };

    int getLength() const {
        return l;
    }
    int getBreadth() const {
        return b;
    }
    int getHeight() const {
        return h;
    }

    long long CalculateVolume() {
        long long volume = (long long) l*b*h;
        return volume;
    }

    bool operator<(Box& other) {
        bool condition1 = l < other.l;
        bool condition2 = b < other.b && l == other.l;
        bool condition3 = h < other.h && b == other.b && l == other.l;
        if(condition1 || condition2 || condition3)
            return true;
        return false;
    }

    friend ostream& operator<<(ostream& out, Box &B) {
        out << B.l << " " << B.b << " " << B.h;
        return out;
    }
};


//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

