---
title: 02 Prepare Video Evidence
nav_order: 4
has_children: true
has_toc: false
---
# 02 Prepare Video Evidence

<p>
  <strong>Open Notebook in Google Colab ➡️</strong>
  <a href="https://colab.research.google.com/github/pgailinas/iterative-video-rag/blob/main/notebooks/02_Prepare_Video_Evidence.ipynb" target="_blank" rel="noopener noreferrer">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle; margin-left: 8px;"/>
  </a>
</p>

## Purpose

This notebook generates evidence metadata for the NExT-QA VideoQA project. Evidence records identify meaningful regions of the original videos using video identifiers, timestamps, segment boundaries, and related metadata.

## Inputs

* Prepared NExT-QA video files from Notebook 01
* NExT-QA question-answer files
  * train.csv
  * val.csv
  * test.csv
* NExT-QA metadata resources
* Project configuration settings
* Shared video and dataset utility functions

## Outputs

* Evidence metadata CSV file
* Video inventory summary
* Evidence metadata summary report
* Sample evidence records for verification

## Processing Workflow

1. Load project configuration and dataset resources.
2. Load NExT-QA metadata and video inventory information.
3. Define the evidence metadata schema and segmentation parameters.
4. Inspect representative videos and extract video properties.
5. Generate evidence metadata records for each processed video.
6. Validate evidence metadata completeness and consistency.
7. Save evidence metadata and summary files.

#### Evidence Metadata Field Definitions

| Field | Description |
|---------|-------------|
| `evidence_id` | Unique identifier assigned to each evidence unit. |
| `video_id` | NExT-QA video identifier associated with the evidence unit. |
| `split` | Dataset split associated with the source video or related QA records (`train`, `val`, or `test`). |
| `source_video_path` | Local path to the source video file used to generate the evidence unit. |
| `evidence_level` | Hierarchy level of the evidence unit. Level `0` typically represents a parent or top-level segment. |
| `parent_evidence_id` | Identifier of the parent evidence unit when hierarchical segmentation is used. Empty for top-level evidence units. |
| `segment_strategy` | Segmentation method used to create the evidence unit, such as fixed-duration, scene-based, or motion-based segmentation. |
| `start_time_sec` | Segment start time in seconds from the beginning of the source video. |
| `midpoint_time_sec` | Segment midpoint time in seconds, used as a representative temporal reference. |
| `end_time_sec` | Segment end time in seconds from the beginning of the source video. |
| `duration_sec` | Duration of the evidence segment in seconds. |
| `start_frame_idx` | Frame index corresponding to the segment start time. |
| `midpoint_frame_idx` | Frame index corresponding to the segment midpoint time. |
| `end_frame_idx` | Frame index corresponding to the segment end time. |
| `fps` | Frames per second of the source video. |
| `frame_count` | Total number of frames in the source video. |
| `width` | Source video frame width in pixels. |
| `height` | Source video frame height in pixels. |
| `motion_score` | Numeric estimate of motion or visual activity within the evidence segment. |
| `scene_change_score` | Numeric estimate of scene-transition strength associated with the evidence segment. |
| `created_by_notebook` | Notebook identifier used to record which notebook generated the evidence metadata. |

## Next Notebook

➡️ [03 Run Baseline VideoQA](03_Run_Baseline_VideoQA.md)

