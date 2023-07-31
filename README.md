# Dynoplan 🦖



<p align="center">
<img src="assets/example1.png" width=60% height=auto>
</p >





The first version [kinodynamic-motion-planning-benchmark](https://github.com/imrCLab/kinodynamic-motion-planning-benchmark) is now deprecated.

## Robots and Problem Description

Kinodynamic motion planning problem are defined in [Dynobench](https://github.com/quimortiz/dynobench)


<p align="center">
<img src="assets/dynobench.png" width=30% height=auto>
</p >


## How to use

we provide several exectuables and libraries for different different use cases

## Testing

Check the tests to learn how to use the code!

## Planners

- Trajectory Optimization (Several Algorithms on top of Differential Dynamic Programming (Croccoddyl))
- RRT*-TO (Geometric Planner RRT* (OMPL)  + Trajectory Optimzation)
- iDb-A* (Iterative disccontinuity bounded search and Trajecgory Optimization)
- SST* (Stable Sparse Tree (OMPL))
- Dbrrt, AO-dbrrt and DBrrtConnect, DB-SST* (coming soon!)

## Building

You can check the Github CI [cmake.yml](.github/workflows/cmake.yml) to see how to compile the project in latest ubuntu (For ubuntu 20.04, we experienced some issues with g++-9, but clang-13 is fine.)

Dependencies:

* Boost
* fcl (0.7)
* yaml-cpp
* Eigen3
* Crocoddyl (1.8)
* OMPL (1.6)

We need OMPL 1.6 for planners RRT + TO and  SST. We recommend to install OMPL in a local directory with -DCMAKE_INSTALL_PREFIX, and use -DCMAKE_PREFIX_PATH here

## Motion Primitives

You will find a small set of motion primitives for each system in  [dynobench](https://github.com/quimortiz/dynobench).

A large set of primitives for each system can be downloaded from Google Drive. This can be done manually with a web browser or using the command line with [gdown](https://github.com/wkentaro/gdown). For example:

```
gdown --fuzzy "https://drive.google.com/file/d/1r_ecGwdfvWnVWxPsvR4d8Hjcayxg5PsB/view?usp=drive_link"
```

All primitive in two ZIP files:  https://drive.google.com/drive/folders/1-Nvctva17I8aFsWvHfdQFWTIDUNWwgcM?usp=drive_link

Primitves per system:

* unicycle1_v0
https://drive.google.com/file/d/15dXqC_OdrI8KjaHRNakYgk9IXLtTeMtt/view?usp=drive_link

* quadrotor_v1 (OMPL-style)
https://drive.google.com/file/d/1r_ecGwdfvWnVWxPsvR4d8Hjcayxg5PsB/view?usp=drive_link

* quadrotor_v0
https://drive.google.com/file/d/1j57kwE5hFgO-46LjStv_zqm6S5BFUsY8/view?usp=drive_link

* Acrobot_v0
  https://drive.google.com/file/d/1mLiTgcpXSI9UHHss4Qt7AIsRwJPbPC2H/view?usp=drive_link

* Roto_Pole_v0
https://drive.google.com/file/d/1KMb4IDgucHN8uWI9YN_W07AhX59tkph_/view?usp=drive_link

* Planar Rotor_v0
https://drive.google.com/file/d/18kI3qXweA4RgvDxtV3vfxnfc_BhX52j8/view?usp=drive_link

* Car1_v0
https://drive.google.com/file/d/1TPX3c8RvMOy9hiaKL-kUE8M61OknDrDK/view?usp=drive_link

* Unicycle 2 _v0
  https://drive.google.com/file/d/1PoK1kbiLRFq_hkv3pVWU0csNr4hap0WX/view?usp=drive_link

* Unicycle 1 v2
https://drive.google.com/file/d/1IvwN-e1jn5P0P1ILaVwSrUnIeBlFxhHI/view?usp=drive_link

* Unicycle 1 v1
https://drive.google.com/file/d/1OLuw5XICTueoZuleXOuD6vNh3PCWfHif/view?usp=drive_link

Tests in `dynoplan` expect he primitves to be in the folder
`cloud/motionsV2/good/NAME_SYSTEM`, e.g.
`cloud/motionsV2/good/acrobot_v0`





## Benchmark

Results of reported in our TRO paper are in folder XX. To replicate the results use commit: `xxxxx`


First, download primitives with:

```
bash -x download_primitives.bash
```

Primitvies are stored in a new `dynomotions_full` directory. Next, move to the `build` directory and run commands:

Benchmark between planners

```
python3 ../benchmark/benchmark.py -m bench -bc    ../benchmark/config/compare.yaml
```

Study of heuristic functions

```
python3 ../benchmark/benchmark.py -m bench_search -bc    ../benchmark/config/bench_search.yaml
```

Study of strategy for trajectoy optimization with free terminal time
```
python3 ../benchmark/benchmark.py -m bench_time -bc    ../benchmark/config/bench_time.yam
```

Study of time spent in each component

```
python3   ../benchmark/benchmark.py -m study  -bc ../benchmark/config/bench_abblation_study.yaml
```

You can modify each config file to change the number of runs, the evaluated problems and the maximum time.
The configurations files we used for `TRO` have prefix `TRO`.

The paramteres for each algorithm are in `.yaml` files inside the `benchmark/config/algs` directory, severalfro example `idbastar_v0.yaml`.







## Citing

If you use or work for academic research, please cite:

```
COOL TRO paper
```


```
@online{hoenigDbADiscontinuityboundedSearch2022,
  title = {Db-A*: Discontinuity-Bounded Search for Kinodynamic Mobile Robot Motion Planning},
  author = {Hoenig, Wolfgang and Ortiz-Haro, Joaquim and Toussaint, Marc},
  year = {2022},
  eprint = {2203.11108},
  eprinttype = {arxiv},
  url = {http://arxiv.org/abs/2203.11108},
  archiveprefix = {arXiv}
}
```
