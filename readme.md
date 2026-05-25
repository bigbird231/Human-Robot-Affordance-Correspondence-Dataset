# Human-Robot Affordance Correspondence Dataset

A paired human-robot affordance contact dataset for manipulation tasks. The dataset contains paired human and robot interaction frames with manually annotated affordance/contact keypoints for human-robot alignment research.

## Overview

This project focuses on:
- Human-robot affordance correspondence
- Tool-centric manipulation representation
- Contact-point alignment
- Task-aware latent representation learning

The dataset is built on top of the Human2Robot dataset and provides manually annotated affordance-contact correspondences between human fingers and robot grippers during manipulation tasks.

## Annotation Definition

Annotations represent corresponding affordance semantics between human and robot interactions.

Example:
- human grasps hammer handle
- robot gripper grasps hammer handle

The goal is to align functionally equivalent interaction regions across embodiments.

## Tasks

Current task categories include:
- grab cube
- grab cup
- grab pencil
- pull/push plate
- push box

## Annotation Tool

The repository includes a lightweight browser-based annotation tool for:
- paired image loading
- contact-point annotation
- coordinate export
- annotated image export

## Notes

This repository is intended for academic and research purposes.

The original Human2Robot dataset belongs to the corresponding authors of the Human2Robot project:
https://huggingface.co/datasets/dannyXSC/HumanAndRobot

## Citation

Citation information will be added after the project is finalized.
