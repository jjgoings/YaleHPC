# YaleHPC
submission scripts for use on HPCs with Yale CRC

To use `submit`, easiest way is to put it into `$HOME/bin` (or otherwise add to path).

To make it executable, just 

```
chmod +x submit 
```

Then, when you want to submit a job, just navigate to your job and

```
submit gaussian16-job.com
```

which will generate `gaussian16-job.sh`, which you can then `sbatch gaussian16-job.sh`.

If you run into issues, just `submit --help` which will give you all the nice command-line options!


