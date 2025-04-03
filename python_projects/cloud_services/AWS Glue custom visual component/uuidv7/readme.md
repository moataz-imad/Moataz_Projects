
# UUIDv7: Custom AWS Glue Visual Component

A custom visual component for AWS Glue Studio that enables generation of UUID version 7 (UUIDv7) identifiers. Designed for high-throughput distributed data pipelines that require time-ordered, unique IDs.

## Table of Contents

- [UUIDv7: Custom AWS Glue Visual Component](#uuidv7-custom-aws-glue-visual-component)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [UUIDv7 Overview](#uuidv7-overview)
  - [Use Cases](#use-cases)

## Introduction

This component adds support for UUIDv7 generation in AWS Glue Studio jobs. UUIDv7 offers time-sortable, high-entropy identifiers that are ideal for large-scale ETL workflows where uniqueness and performance are critical.

## UUIDv7 Overview

UUID version 7 is a proposed IETF standard that combines Unix epoch timestamps with random bits. It maintains global uniqueness while preserving insertion order, making it efficient for sorting and indexing.

Key features:
- Time-ordered
- Low collision rate
- Suitable for distributed systems

## Use Cases

- Record deduplication
- Event tracking
- Surrogate keys in data lakes
- Log and event stream processing


