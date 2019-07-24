def DNA(genome):
    genelist=[]
    gene=''
    start=0
    end=0
    for i in range(len(genome)):
        if genome[i:i+3]=="ATG":
            start=i
            sequence=""
            while start<len(genome[start:]):
                if genome[start:start+3]=="TAG" or genome[start:start+3]=="TAA" or genome[start:start+3]=="TGA":
                    end=genome[start:start+3]
                start+=3
        gene+=genome[start:end]
    return gene


def main():
    genome=input("Enter genome: ")
    print(DNA(genome))

if __name__ == '__main__':
    main()
