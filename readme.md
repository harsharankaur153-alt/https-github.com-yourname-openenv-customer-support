# Customer Support OpenEnv

## Overview
This environment simulates real-world customer support workflows.

## Tasks
- Easy: classify query
- Medium: prioritize issue
- Hard: generate response

## Features
- Incremental reward shaping
- Deterministic grading
- OpenAI-based inference

## Setup
docker build -t openenv .
docker run openenv

## Baseline
Average reward: ~0.7