#!/usr/bin/env python3

import json
import argparse

import simulation
import general
import alignment

parser = argparse.ArgumentParser(
    description='Script to run a simulation and reconstruction of the PANDA '
    'Luminosity Detector from parameter config files.',
    formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('sim_params', metavar='sim_params', type=str,
                    nargs=1, help='Path to simulation properties json file\n')
parser.add_argument('reco_params', metavar='reco_params', type=str,
                    nargs=1, help='Path to reconstruction properties json file\n')

parser = general.addDebugArgumentsToParser(parser)

args = parser.parse_args()

with open(args.sim_params[0], 'r') as json_file:
    sim_params = json.load(json_file)

with open(args.reco_params[0], 'r') as json_file:
    reco_params = json.load(json_file)

align_params = alignment.getAlignmentParameters(reco_params)

simulation.startSimulationAndReconstruction(
    sim_params, align_params, reco_params,
    force_level=args.force_level,
    debug=args.debug, use_devel_queue=args.use_devel_queue)
