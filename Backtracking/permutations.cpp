//Print all permutations of given string which do not have given substring
bool permute(String string1,int l,int r){
    if(l==r){
            cout << string1;
            return;}    
    else
    {
        for(int i=l;i<=r;i++){
            swap(string1[l],string1[i]);
            permute(string1,l+1,r); 
            swap(string1[l],string1[i]);    
    }
    }
permute("abc","ab",0,2);            
