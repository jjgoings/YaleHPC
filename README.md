# YaleHPC
Gaussian 16 or Q-Chem  submission scripts for use on HPCs (primarily Grace) with Yale CRC

**Note: you need to be given access to either G16 or Q-Chem before use**

## Installation

To use `submit`, easiest way is to put it into `$HOME/bin` (or otherwise add to `$PATH`).

To make it executable, just 

```
chmod +x submit 
```

## Usage
The script will automatically detect what type of job you want to run based on the extension. Q-Chem is `.in` or `.inp` and G16 is `.com` or `.gjf`. The script will gently scream at you if the file does not exist or is badly named, and will give you advice on how to fix it.

Anyway.

Say you want to run a G16 job called `gaussian16-job.com`. Just navigate to your job and

```
submit gaussian16-job.com
```

which will generate the submit script `gaussian16-job.sh`, which you can then 

```
sbatch gaussian16-job.sh
```

### Command-line options
Aside from the required input file, you can also

#### Set number of CPU threads (defaults to 24)

```
submit -nt <NUMBER_THREADS>
```

#### Set time to run (default is 4 hours)

```
submit -t <TIME_IN_HOURS>
```

#### Set partition (default is `pi_hammes_schiffer`, so you'll need to change if you aren't in our group! `day` is a good choice on Grace)

```
submit -p <PARTITION>
```


## Help
If you run into issues, just `submit --help` which will give you all the nice command-line options!

```
user@grace:~$ submit --help
usage: submit [-h] [-nt N] [-p P] [-t T] infile

Prepare Gaussian 16 or Q-Chem submit script on Grace.

positional arguments:
  infile               Gaussian 16 or Q-Chem input file

optional arguments:
  -h, --help           show this help message and exit
  -nt N, --nthreads N  CPUs-per-node
  -p P, --partition P  partition
  -t T, --time T       time (hours)
```

Feel free to modify the submit script afterward to your liking, since not all the options you may wish to use (such as email on completetion) are not included by default.

Happy computing!


