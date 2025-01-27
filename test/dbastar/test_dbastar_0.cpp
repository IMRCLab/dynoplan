
#include "idbastar/dbastar/dbastar.hpp"

// #define BOOST_TEST_MODULE test module name
// #define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>

#include "Eigen/Core"
#include <boost/program_options.hpp>

// #include "collision_checker.hpp"

// save data without the cluster stuff

#include <filesystem>
#include <random>
#include <regex>
#include <type_traits>

#include <filesystem>
#include <regex>

#include "dynobench/motions.hpp"
#include <Eigen/Dense>
#include <iostream>

#define DYNOBENCH_BASE "../../dynobench/"

using namespace dynoplan;
using namespace dynobench;

BOOST_AUTO_TEST_CASE(test_bugtrap_heu) {

  Problem problem(DYNOBENCH_BASE +
                  std::string("envs/unicycle1_v0/bugtrap_0.yaml"));
  problem.models_base_path = DYNOBENCH_BASE + std::string("models/");
  Options_dbastar options_dbastar;
  options_dbastar.search_timelimit = 1e5; // in ms
  options_dbastar.max_motions = 30;
  options_dbastar.heuristic = 0;
  options_dbastar.motionsFile =
      "../../data/motion_primitives/unicycle1_v0/"
      "unicycle1_v0__ispso__2023_04_03__14_56_57.bin.less.bin";

  // "/home/quim/stg/wolfgang/kinodynamic-motion-planning-benchmark/cloud/"
  // "motionsV2/good/unicycle1_v0/"
  // "unicycle1_v0__ispso__2023_04_03__14_56_57.bin";
  options_dbastar.use_nigh_nn = 1;
  Out_info_db out_info_db;
  Trajectory traj_out;
  dbastar(problem, options_dbastar, traj_out, out_info_db);
  BOOST_TEST(out_info_db.solved);
  CSTR_(out_info_db.cost);
  BOOST_TEST(out_info_db.cost < 60.);
}
