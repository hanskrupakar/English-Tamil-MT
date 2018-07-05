import argparse
import popen2 
import sys 

class Stemmer:
    def __init__(self):
            self.stemmer = "./snowball-with-tamil/stemwords"
        
    def stemWord(self,str):
        self.fin, self.fout = popen2.popen2(self.stemmer + " -l ta")
        self.fout.write(str)
        self.fout.write("\n")
        self.fout.close()
        res=self.fin.readlines()
        self.fin.close()
        return res
        
if __name__=='__main__':
    
    ap = argparse.ArgumentParser()
    ap.add_argument('--src_file', help='Path to MT output file', default='/home/hans/res.txt')
    ap.add_argument('--targ_file', help='Path to reference translation file', default='/home/hans/targ.txt')
    args = ap.parse_args()
    
    with open(args.src_file, 'r') as f:
        ref = [x.strip().split(' ') for x in f.readlines()]
        rwords = [x for y in ref for x in y]
    
    with open(args.targ_file, 'r') as f:
        targ = [x.strip().split(' ') for x in f.readlines()]
        twords = [x for y in targ for x in y]
        
    unique_src_words = list(set(rwords))
    unique_targ_words = list(set(twords))
    
    stemmer = Stemmer()
    
    matches, F_mean = 0, 0
    for sent1, sent2 in zip(ref, targ):
        for w1 in sent1:
            for w2 in sent2:
                if w1 in w2:
                    matches+=1
                    break
                if stemmer.stemWord(w1)[0] in w2:
                    matches+=1
                    break
                    
        precision, recall = float(matches)/len(sent1), float(matches)/len(sent2)
        matches=0
        if precision>0 and recall>0:
            F_mean += precision*recall*10/float(recall+9*precision)
    
    F_mean/=len(ref)
    
    print ('METEOR SCORE:', F_mean)        
       
    #rstr = 'snowball-with-tamil/stemwords -l ta -i /home/hans/src.txt -o /home/hans/src_stemmed.txt'
    #rstr2 = 'snowball-with-tamil/stemwords -l ta -i /home/hans/target.txt -o /home/hans/target_stemmed.txt'
    
    #popen2.popen2(rstr)
    #popen2.popen2(rstr2)
    
    
