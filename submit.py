#!/bin/python
from __future__ import print_function
import sys
import os
import argparse

class SlurmJob(object):
    def __init__(self,args):
        # Check input actually exists
        if not os.path.isfile(args.infile):
            sys.exit('The input file does not exist!')
        
        # Make sure we have the correct extension
        infile = args.infile.split('.')
        self.software = None
        try:
            extension = infile[1]
        except IndexError:
            sys.exit('Q-Chem input file must have .in or .inp extension')
        if (extension == 'in') or (extension == 'inp'):
            print('Extension: ',extension,'; assuming a Q-Chem job')
            self.software = 'qchem'
        elif (extension == 'com') or (extension == 'gjf'):
            print('Extension: ',extension,'; assuming a Gaussian 16 job')
            self.software = 'g16'
        else:
            sys.exit('Q-Chem input file must have .in or .inp extension \n \
                      Gaussian input file must have .com or .gjf extension \n \
                      ...please make the appropriate changes and resubmit.')
     
        self.name      = infile[0]
        self.infile    = args.infile 
        self.threads   = args.nthreads
        self.partition = args.partition
        self.time      = args.time
        self.script    = self.name+'.sh'

    def write_slurm_script(self):
        with open(self.script,'w') as f:
           f.write("#!/bin/bash\n")
           f.write("#SBATCH --job-name="+self.name+"\n")
           f.write("#SBATCH --nodes=1\n")
           f.write("#SBATCH --cpus-per-task="+str(self.threads)+"\n")
           f.write("#SBATCH --partition="+self.partition+"\n")
           f.write("#SBATCH -t "+str(self.time).zfill(2)+":00:00\n")
           f.write("\n")
           if self.software == 'qchem':
               f.write(self.software+" -nt ${SLURM_CPUS_ON_NODE} "+self.infile+" "+self.name+".out\n")
               f.write("\n")
               f.write("rm slurm-${SLURM_JOB_ID}.out")
           elif self.software == 'g16':
               f.write("module load Apps/Gaussian/2016-A03\n")
               f.write("\n")
               f.write(self.software+" < "+self.infile+" > "+self.name+".log\n")
               f.write("\n")
               f.write("rm slurm-${SLURM_JOB_ID}.out\n")
               f.write("rm core.*")

        print(self.software+' submission script written to '+self.script) 
        print('To submit, do "sbatch '+self.script+'"') 

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prepare Gaussian 16 or Q-Chem submit script on Grace.')
    parser.add_argument("infile", help="Gaussian 16 or Q-Chem input file")
    parser.add_argument("-nt", "--nthreads",metavar='N', help="CPUs-per-node",type=int,default=24)
    parser.add_argument("-p","--partition",metavar='P',help="partition",default="pi_hammes_schiffer")
    parser.add_argument("-t","--time",metavar='T',help="time (hours)",type=int,default=4)
    args = parser.parse_args()

    slurmjob = SlurmJob(args)
    slurmjob.write_slurm_script()

