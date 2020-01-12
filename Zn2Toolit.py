class Search:
    def __init__(self):
        self.state = True
    def toolsel(self):
        sel = str(input('Select Tool: '))
        if sel == 'CPU Zn2' or sel=='cpu zn2' or sel=='CPU ZN2' or sel =='Cpu zn2' or sel=='Cpu Zn2':
            import npAccExtractor
        elif sel == 'GPU Zn2' or sel == 'gpu zn2' or sel == 'GPU ZN2' or sel == 'Gpu zn2' or sel == 'Gpu Zn2':
            import GpuAccWcupy
        elif sel == 'Converter' or sel == 'converter':
            import extractor
        elif sel == 'Combos' or sel == 'combos':
            import combos
        else:
            print('Tool not found')
            print('Exiting...')

    def listing(self):
        print('Converter - Converts .lc file to .csv file readable by the Zn2 tools')
        print('CPU Zn2 - Zn2 statistic that runs on the CPU (Works for all builds)')
        print('GPU Zn2 - Zn2 statistic the runs on the GPU (Only works with CUDA devices i.e Nvidia GPUs)')
        print('Combos - Combines all files for a data set, plots, and allows search for numerical results')

def main():
    S = Search()
    state = True
    print('########## Zn2 Toolkit ##########')
    dir = str(input('See a list of all tools(y/n)? [n] '))
    if dir == 'y' or dir=='Y':
        S.listing()
    else:
        pass
    S.toolsel()
main()



