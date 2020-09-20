

class Student{
    public:
    int m[5], sum=0;

    void input()
    {
        for (int i=0;i<5;i++){
            cin>>m[i];
            sum=sum+m[i];
        }
    }

    int calculateTotalScore()
    {
        return sum;
    }
};

