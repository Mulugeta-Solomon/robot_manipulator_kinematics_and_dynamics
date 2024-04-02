# Kinematics and Velocity Relation using DH Method

This repository contains Python code for calculating the forward kinematics, Jacobian matrices, and Lagrangian for robot manipulators using the Denavit-Hartenberg (DH) method. The code is implemented using the Sympy library.

## Introduction

The Denavit-Hartenberg (DH) method is commonly used in robotics for modeling the kinematics of robotic manipulators. This method allows us to derive the forward kinematics equations, which describe the relationship between joint variables and end-effector position and orientation.

## Contents

- [DH Table](#dh-table)
- [Forward Kinematics](#forward-kinematics)
- [Jacobian Calculation](#jacobian-calculation)
- [Lagrangian Formulation](#lagrangian-formulation)

## DH Table

The DH table for the 6-DOF robot manipulator used in this project is as follows:
| Link | θᵢ       | dᵢ       | aᵢ       | αᵢ       |
|------|----------|----------|----------|----------|
| 1    | θ₁       | 0        | l₁       | 0        |
| 2    | θ₂       | 0        | l₂       | 0        |
| 3    | θ₃       | 0        | l₃       | 0        |
| 4    | θ₄       | 0        | 0        | π/2      |
| 5    | θ₅       | 0        | 0        | π/2      |
| 6    | θ₆       | h₁       | 0        | 0        |


## Forward Kinematics

The forward kinematics equations are derived using the DH method to obtain the transformation matrix from the base frame to the end-effector frame. This transformation is calculated for each joint and represented in homogeneous matrix form.

## Jacobian Calculation

The Jacobian matrix is computed to describe the relationship between joint velocities and end-effector linear and angular velocities. The Jacobian matrix is derived based on the partial derivatives of the forward kinematics equations with respect to the joint variables.

## Lagrangian Formulation

The Lagrangian formulation is utilized to derive the dynamic equations of motion for the robotic manipulator. The Lagrangian is calculated based on the kinetic and potential energies of the system.

## Usage

To use the code, simply run the Python scripts provided in this repository. Make sure to have the Sympy library installed.

```bash
pip install sympy
python Report_2.ipyb


