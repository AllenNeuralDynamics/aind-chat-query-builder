"""Script to build filter queries with v2 data schema"""

import json


def get_simple_v2_prompt(query: str):
    """
    Prompt specific to v2 data schema
    Enables simple filter query building and prompt caching
    """

    sample_acquisition = json.dumps(
        {
            "acquisition": {
                "object_type": "Acquisition",
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/acquisition.py",
                "schema_version": "2.0.34",
                "subject_id": "752014",
                "specimen_id": None,
                "acquisition_start_time": "2025-03-12 09:33:26.337641-07:00",
                "acquisition_end_time": "2025-03-12 10:48:33.715103-07:00",
                "experimenters": ["Huy Nguyen"],
                "protocol_id": [""],
                "ethics_review_id": None,
                "instrument_id": "446_6B_20250304",
                "acquisition_type": "Uncoupled Without Baiting",
                "notes": " notes",
                "coordinate_system": None,
                "calibrations": [],
                "maintenance": [],
                "data_streams": [
                    {
                        "object_type": "Data stream",
                        "stream_start_time": "2025-03-03 22:47:07-08:00",
                        "stream_end_time": "2025-03-04 03:20:16-08:00",
                        "modalities": [
                            {
                                "name": "Selective plane illumination microscopy",
                                "abbreviation": "SPIM",
                            }
                        ],
                        "code": None,
                        "notes": "\nLaser power is in percentage of total, it needs calibration",
                        "active_devices": ["639", "561", "488", "LCT 3.6x"],
                        "configurations": [
                            {
                                "object_type": "Imaging config",
                                "device_name": "unknown",
                                "channels": [
                                    {
                                        "object_type": "Channel",
                                        "channel_name": "488",
                                        "intended_measurement": None,
                                        "detector": {
                                            "object_type": "Detector config",
                                            "device_name": "unknown_detector",
                                            "exposure_time": 1,
                                            "exposure_time_unit": "millisecond",
                                            "trigger_type": "Internal",
                                            "compression": None,
                                        },
                                        "additional_device_names": None,
                                        "light_sources": [
                                            {
                                                "object_type": "Laser config",
                                                "device_name": "Ex_488",
                                                "wavelength": 488,
                                                "wavelength_unit": "nanometer",
                                                "power": None,
                                                "power_unit": None,
                                            }
                                        ],
                                        "variable_power": False,
                                        "excitation_filters": None,
                                        "emission_filters": [],
                                        "emission_wavelength": None,
                                        "emission_wavelength_unit": "nanometer",
                                    },
                                ],
                                "coordinate_system": None,
                                "images": [],
                                "sampling_strategy": None,
                            },
                            {
                                "object_type": "Sample chamber config",
                                "device_name": "440_SmartSPIM2_20250114",
                                "chamber_immersion": {
                                    "object_type": "Immersion",
                                    "medium": "other",
                                    "refractive_index": 1.517,
                                },
                                "sample_immersion": {
                                    "object_type": "Immersion",
                                    "medium": "other",
                                    "refractive_index": 1.5202,
                                },
                            },
                        ],
                        "connections": [],
                    }
                ],
                "stimulus_epochs": [
                    {
                        "object_type": "Stimulus epoch",
                        "stimulus_start_time": "2025-03-12 09:33:26.337641-07:00",
                        "stimulus_end_time": "2025-03-12 10:48:33.715103-07:00",
                        "stimulus_name": "The behavior auditory go cue",
                        "code": None,
                        "stimulus_modalities": ["Auditory"],
                        "performance_metrics": {
                            "object_type": "Performance metrics",
                            "output_parameters": {
                                "meta": {
                                    "box": "446-6-B",
                                    "session_run_time_in_min": 75,
                                },
                                "performance": {
                                    "foraging_efficiency": 0.674567000911577,
                                    "foraging_efficiency_with_actual_random_seed": 0.6867749419953596,
                                },
                                "task_parameters": {
                                    "BlockBeta": "10",
                                    "BlockMax": "35",
                                    "BlockMin": "20",
                                    "DelayBeta": "0.0",
                                    "DelayMax": "1.0",
                                    "DelayMin": "1.0",
                                    "ITIBeta": "3.0",
                                    "ITIMax": "15.0",
                                    "ITIMin": "2.0",
                                    "LeftValue_volume": "2.00",
                                    "RightValue_volume": "2.00",
                                    "Task": "Uncoupled Without Baiting",
                                    "reward_probability": "0.1, 0.5, 0.9",
                                },
                                "water": {
                                    "water_after_session": 0.65,
                                    "water_day_total": 1.252,
                                    "water_in_session_foraging": 0.592,
                                    "water_in_session_manual": 0.010000000000000009,
                                    "water_in_session_total": 0.602,
                                },
                            },
                            "reward_consumed_during_epoch": "592.0",
                            "reward_consumed_unit": "microliter",
                            "trials_total": 620,
                            "trials_finished": 606,
                            "trials_rewarded": 296,
                        },
                        "notes": "notes",
                        "active_devices": ["Stimulus Speaker"],
                        "configurations": [
                            {
                                "object_type": "Speaker config",
                                "device_name": "Stimulus Speaker",
                                "volume": 73,
                                "volume_unit": "decibels",
                            }
                        ],
                        "training_protocol_name": None,
                        "curriculum_status": None,
                    }
                ],
                "subject_details": {
                    "object_type": "Acquisition subject details",
                    "animal_weight_prior": "29.0",
                    "animal_weight_post": "24.0",
                    "weight_unit": "gram",
                    "anaesthesia": None,
                    "mouse_platform_name": "mouse_tube_foraging",
                    "reward_consumed_total": "592.0",
                    "reward_consumed_unit": "microliter",
                },
            }
        }
    )

    sample_data_description = json.dumps(
        {
            "data_description": {
                "object_type": "Data description",
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/data_description.py",
                "schema_version": "2.0.12",
                "license": "CC-BY-4.0",
                "subject_id": "752014",
                "creation_time": "2025-03-12 10:48:33.715103-07:00",
                "tags": None,
                "name": "behavior_752014_2025-03-12_09-33-26",
                "institution": {
                    "name": "Allen Institute for Neural Dynamics",
                    "abbreviation": "AIND",
                    "registry": "Research Organization Registry (ROR)",
                    "registry_identifier": "04szwah67",
                },
                "funding_source": [
                    {
                        "object_type": "Funding",
                        "funder": {
                            "name": "Allen Institute",
                            "abbreviation": "AI",
                            "registry": "Research Organization Registry (ROR)",
                            "registry_identifier": "03cpe7c52",
                        },
                        "grant_number": None,
                        "fundee": [
                            {
                                "object_type": "Person",
                                "name": "unknown",
                                "registry": "Open Researcher and Contributor ID (ORCID)",
                                "registry_identifier": None,
                            }
                        ],
                    }
                ],
                "data_level": "raw",
                "group": None,
                "investigators": [
                    {
                        "object_type": "Person",
                        "name": "Cindy Poo",
                        "registry": "Open Researcher and Contributor ID (ORCID)",
                        "registry_identifier": None,
                    },
                    {
                        "object_type": "Person",
                        "name": "Jeremiah Cohen",
                        "registry": "Open Researcher and Contributor ID (ORCID)",
                        "registry_identifier": None,
                    },
                ],
                "project_name": "Behavior Platform",
                "restrictions": None,
                "modalities": [
                    {"name": "Behavior", "abbreviation": "behavior"}
                ],
                "data_summary": None,
            },
        }
    )

    sample_instrument = json.dumps(
        {
            "instrument": {
                "object_type": "Instrument",
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/instrument.py",
                "schema_version": "2.0.38",
                "location": None,
                "instrument_id": "446_6B_20250304",
                "modification_date": "2025-03-04",
                "modalities": [],
                "calibrations": [
                    {
                        "object_type": "Volume calibration",
                        "device_name": "Lick spout Right",
                        "calibration_date": "2024-12-03 00:00:00-08:00",
                        "description": "Volume measured for various solenoid opening times",
                        "input": [0.0202],
                        "input_unit": "second",
                        "repeats": None,
                        "output": [1.85],
                        "output_unit": "microliter",
                        "fit": None,
                        "notes": None,
                    },
                ],
                "coordinate_system": {
                    "object_type": "Coordinate system",
                    "name": "BREGMA_ARI",
                    "origin": "Bregma",
                    "axes": [
                        {
                            "object_type": "Axis",
                            "name": "AP",
                            "direction": "Posterior_to_anterior",
                        },
                        {
                            "object_type": "Axis",
                            "name": "ML",
                            "direction": "Left_to_right",
                        },
                        {
                            "object_type": "Axis",
                            "name": "SI",
                            "direction": "Superior_to_inferior",
                        },
                    ],
                    "axis_unit": "millimeter",
                },
                "temperature_control": None,
                "notes": None,
                "connections": [
                    {
                        "object_type": "Connection",
                        "source_device": "Right size of face camera",
                        "source_port": None,
                        "target_device": "W10DT714672",
                        "target_port": None,
                        "send_and_receive": False,
                    }
                ],
                "components": [
                    {
                        "object_type": "Objective",
                        "name": "LCT 3.6x",
                        "serial_number": "Unknown",
                        "manufacturer": {
                            "name": "Thorlabs",
                            "abbreviation": None,
                            "registry": "Research Organization Registry (ROR)",
                            "registry_identifier": "04gsnvb07",
                        },
                        "model": "TL4X-SAP",
                        "additional_settings": {},
                        "notes": "Thorlabs TL4X-SAP with LifeCanvas dipping cap and correction optics.",
                        "numerical_aperture": "0.2",
                        "magnification": "3.6",
                        "immersion": "multi",
                        "objective_type": None,
                    },
                    {
                        "object_type": "Detector",
                        "name": "Camera",
                        "serial_number": "001107",
                        "manufacturer": {
                            "name": "Hamamatsu",
                            "abbreviation": None,
                            "registry": "Research Organization Registry (ROR)",
                            "registry_identifier": "03natb733",
                        },
                        "model": "C14440-20UP",
                        "additional_settings": {},
                        "notes": None,
                        "detector_type": "Camera",
                        "data_interface": "USB",
                        "cooling": "Water",
                        "frame_rate": None,
                        "frame_rate_unit": "hertz",
                        "immersion": None,
                        "chroma": None,
                        "sensor_width": None,
                        "sensor_height": None,
                        "size_unit": "pixel",
                        "sensor_format": None,
                        "sensor_format_unit": None,
                        "bit_depth": None,
                        "bin_mode": "No binning",
                        "bin_width": None,
                        "bin_height": None,
                        "bin_unit": "pixel",
                        "gain": None,
                        "crop_offset_x": None,
                        "crop_offset_y": None,
                        "crop_width": None,
                        "crop_height": None,
                        "crop_unit": "pixel",
                        "recording_software": None,
                        "driver": None,
                        "driver_version": None,
                    },
                    {
                        "object_type": "Laser",
                        "name": "Ex_488",
                        "serial_number": "",
                        "manufacturer": {
                            "name": "Vortran",
                            "abbreviation": None,
                            "registry": None,
                            "registry_identifier": None,
                        },
                        "model": "Stradus",
                        "additional_settings": {},
                        "notes": "All lasers controlled via Vortran VersaLase System",
                        "wavelength": 488,
                        "wavelength_unit": "nanometer",
                        "coupling": "Single-mode fiber",
                        "coupling_efficiency": None,
                        "coupling_efficiency_unit": "percent",
                    },
                    {
                        "object_type": "Filter",
                        "name": "Em_525",
                        "serial_number": "Unknown-1",
                        "manufacturer": {
                            "name": "Semrock",
                            "abbreviation": None,
                            "registry": None,
                            "registry_identifier": None,
                        },
                        "model": "FF03-525/50-32",
                        "additional_settings": {},
                        "notes": None,
                        "filter_type": "Band pass",
                        "cut_off_wavelength": None,
                        "cut_on_wavelength": None,
                        "center_wavelength": None,
                        "wavelength_unit": "nanometer",
                    },
                    {
                        "object_type": "Motorized stage",
                        "name": "Focus stage",
                        "serial_number": "6244",
                        "manufacturer": {
                            "name": "Applied Scientific Instrumentation",
                            "abbreviation": "ASI",
                            "registry": None,
                            "registry_identifier": None,
                        },
                        "model": "LS-100",
                        "additional_settings": {},
                        "notes": None,
                        "travel": "100",
                        "travel_unit": "millimeter",
                        "firmware": None,
                    },
                    {
                        "object_type": "Scanning stage",
                        "name": "Sample stage Z",
                        "serial_number": "6243",
                        "manufacturer": {
                            "name": "Applied Scientific Instrumentation",
                            "abbreviation": "ASI",
                            "registry": None,
                            "registry_identifier": None,
                        },
                        "model": "LS-50",
                        "additional_settings": {},
                        "notes": None,
                        "travel": "50",
                        "travel_unit": "millimeter",
                        "firmware": None,
                        "stage_axis_direction": "Detection axis",
                        "stage_axis_name": "Z",
                    },
                    {
                        "object_type": "Additional imaging device",
                        "name": "tunable lens",
                        "serial_number": "Unknown-1",
                        "manufacturer": {
                            "name": "Optotune",
                            "abbreviation": None,
                            "registry": None,
                            "registry_identifier": None,
                        },
                        "model": "EL-16-40-TC",
                        "additional_settings": {},
                        "notes": "Electrically tunable lens",
                        "imaging_device_type": "Other",
                    },
                    {
                        "object_type": "Microscope",
                        "name": "440_SmartSPIM2_20250114",
                        "serial_number": None,
                        "manufacturer": None,
                        "model": None,
                        "additional_settings": None,
                        "notes": None,
                    },
                    {
                        "object_type": "Tube",
                        "name": "mouse_tube_foraging",
                        "serial_number": None,
                        "manufacturer": {
                            "name": "Custom",
                            "abbreviation": None,
                            "registry": None,
                            "registry_identifier": None,
                        },
                        "model": None,
                        "additional_settings": {},
                        "notes": None,
                        "diameter": "3.0",
                        "diameter_unit": "centimeter",
                    },
                    {
                        "object_type": "Lick spout assembly",
                        "name": "LickSpoutAssembly 3489",
                        "lick_spouts": [
                            {
                                "object_type": "Lick spout",
                                "name": "Left lick spout",
                                "serial_number": None,
                                "manufacturer": {
                                    "name": "Other",
                                    "abbreviation": None,
                                    "registry": None,
                                    "registry_identifier": None,
                                },
                                "model": None,
                                "additional_settings": {},
                                "notes": " (v1v2 upgrade): 'manufacturer' field was missing, defaulting to 'Other'.",
                                "spout_diameter": "1.2",
                                "spout_diameter_unit": "millimeter",
                                "solenoid_valve": {
                                    "object_type": "Device",
                                    "name": "Solenoid Left",
                                    "serial_number": None,
                                    "manufacturer": {
                                        "name": "The Lee Company",
                                        "abbreviation": None,
                                        "registry": None,
                                        "registry_identifier": None,
                                    },
                                    "model": "LHDA1233415H",
                                    "additional_settings": {},
                                    "notes": None,
                                },
                                "lick_sensor": {
                                    "object_type": "Device",
                                    "name": "Lick Sensor Left",
                                    "serial_number": None,
                                    "manufacturer": {
                                        "name": "Janelia Research Campus",
                                        "abbreviation": "Janelia",
                                        "registry": "Research Organization Registry (ROR)",
                                        "registry_identifier": "013sk6x84",
                                    },
                                    "model": None,
                                    "additional_settings": {},
                                    "notes": None,
                                },
                                "lick_sensor_type": "Capacitive",
                            },
                        ],
                        "motorized_stage": {
                            "object_type": "Motorized stage",
                            "name": "AIND lick spout stage",
                            "serial_number": None,
                            "manufacturer": {
                                "name": "Allen Institute for Neural Dynamics",
                                "abbreviation": "AIND",
                                "registry": "Research Organization Registry (ROR)",
                                "registry_identifier": "04szwah67",
                            },
                            "model": None,
                            "additional_settings": {},
                            "notes": "https://allenneuraldynamics.github.io/Bonsai.AllenNeuralDynamics/articles/aind-manipulator.html",
                            "travel": "30",
                            "travel_unit": "millimeter",
                            "firmware": None,
                        },
                    },
                    {
                        "object_type": "Speaker",
                        "relative_position": [],
                        "coordinate_system": None,
                        "transform": None,
                        "name": "Stimulus Speaker",
                        "serial_number": None,
                        "manufacturer": {
                            "name": "Tymphany",
                            "abbreviation": None,
                            "registry": None,
                            "registry_identifier": None,
                        },
                        "model": "XT25SC90-04",
                        "additional_settings": {},
                        "notes": None,
                    },
                    {
                        "object_type": "Camera assembly",
                        "relative_position": ["Inferior"],
                        "coordinate_system": None,
                        "transform": None,
                        "name": "Bottom Camera assembly",
                        "target": "Body",
                        "camera": {
                            "object_type": "Camera",
                            "name": "bottom of face camera",
                            "serial_number": "23350946",
                            "manufacturer": {
                                "name": "Teledyne FLIR",
                                "abbreviation": "FLIR",
                                "registry": "Research Organization Registry (ROR)",
                                "registry_identifier": "01j1gwp17",
                            },
                            "model": "Blackfly S BFS-U3-04S2M",
                            "additional_settings": {},
                            "notes": None,
                            "detector_type": "Camera",
                            "data_interface": "USB",
                            "cooling": "Air",
                            "frame_rate": None,
                            "frame_rate_unit": "hertz",
                            "immersion": None,
                            "chroma": "Monochrome",
                            "sensor_width": 720,
                            "sensor_height": 540,
                            "size_unit": "pixel",
                            "sensor_format": "1/2.9",
                            "sensor_format_unit": "inch",
                            "bit_depth": None,
                            "bin_mode": "No binning",
                            "bin_width": None,
                            "bin_height": None,
                            "bin_unit": "pixel",
                            "gain": None,
                            "crop_offset_x": None,
                            "crop_offset_y": None,
                            "crop_width": None,
                            "crop_height": None,
                            "crop_unit": "pixel",
                            "recording_software": None,
                            "driver": None,
                            "driver_version": None,
                        },
                        "lens": {
                            "object_type": "Lens",
                            "name": "Behavior Video Lens Bottom of face",
                            "serial_number": None,
                            "manufacturer": {
                                "name": "Other",
                                "abbreviation": None,
                                "registry": None,
                                "registry_identifier": None,
                            },
                            "model": "LM25HC",
                            "additional_settings": {},
                            "notes": "Manufacturer is Kowa",
                        },
                        "filter": None,
                    },
                    {
                        "object_type": "Harp device",
                        "name": "harp clock synchronization board",
                        "serial_number": None,
                        "manufacturer": {
                            "name": "Champalimaud Foundation",
                            "abbreviation": "Champalimaud",
                            "registry": "Research Organization Registry (ROR)",
                            "registry_identifier": "03g001n57",
                        },
                        "model": None,
                        "additional_settings": {},
                        "notes": None,
                        "data_interface": "USB",
                        "channels": [],
                        "firmware_version": None,
                        "hardware_version": None,
                        "harp_device_type": {
                            "whoami": 1152,
                            "name": "ClockSynchronizer",
                        },
                        "core_version": "",
                        "tag_version": None,
                        "is_clock_generator": True,
                    },
                    {
                        "object_type": "Light emitting diode",
                        "name": "IR LED",
                        "serial_number": None,
                        "manufacturer": {
                            "name": "Thorlabs",
                            "abbreviation": None,
                            "registry": "Research Organization Registry (ROR)",
                            "registry_identifier": "04gsnvb07",
                        },
                        "model": "M810L5",
                        "additional_settings": {},
                        "notes": None,
                        "wavelength": 810,
                        "wavelength_unit": "nanometer",
                        "bandwidth": None,
                        "bandwidth_unit": "nanometer",
                    },
                    {
                        "object_type": "Enclosure",
                        "name": "Behavior enclosure",
                        "serial_number": None,
                        "manufacturer": {
                            "name": "Allen Institute for Neural Dynamics",
                            "abbreviation": "AIND",
                            "registry": "Research Organization Registry (ROR)",
                            "registry_identifier": "04szwah67",
                        },
                        "model": None,
                        "additional_settings": {},
                        "notes": " (v1v2 upgrade): Scale is width/length/height",
                        "size": {
                            "object_type": "Scale",
                            "scale": [54, 54, 54],
                        },
                        "size_unit": "centimeter",
                        "internal_material": "",
                        "external_material": "",
                        "grounded": False,
                        "laser_interlock": False,
                        "air_filtration": False,
                    },
                    {
                        "object_type": "Device",
                        "name": "Right size of face camera",
                        "serial_number": None,
                        "manufacturer": None,
                        "model": None,
                        "additional_settings": None,
                        "notes": "(v1v2 upgrade) This device was not found in the components list, but is referenced in connections.",
                    },
                ],
            },
        }
    )

    sample_procedures = json.dumps(
        {
            "procedures": {
                "object_type": "Procedures",
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/procedures.py",
                "schema_version": "2.0.32",
                "subject_id": "752014",
                "subject_procedures": [
                    {
                        "object_type": "Surgery",
                        "protocol_id": "dx.doi.org/10.17504/protocols.io.kqdg392o7g25/v2",
                        "start_date": "2024-09-18",
                        "experimenters": ["NSB-6894"],
                        "ethics_review_id": "2109",
                        "animal_weight_prior": 25,
                        "animal_weight_post": 28.4,
                        "weight_unit": "gram",
                        "anaesthesia": {
                            "object_type": "Anaesthetic",
                            "anaesthetic_type": "isoflurane",
                            "duration": 180,
                            "duration_unit": "minute",
                            "level": 1.5,
                        },
                        "workstation_id": "SWS 9",
                        "coordinate_system": None,
                        "measured_coordinates": None,
                        "procedures": [
                            {
                                "object_type": "Headframe",
                                "protocol_id": None,
                                "headframe_type": "unknown",
                                "headframe_part_number": "unknown",
                                "headframe_material": None,
                                "well_part_number": None,
                                "well_type": None,
                            },
                            {
                                "object_type": "Brain injection",
                                "injection_materials": [
                                    {
                                        "object_type": "Viral material",
                                        "name": "unknown",
                                        "tars_identifiers": {
                                            "object_type": "Tars virus identifiers",
                                            "virus_tars_id": "AiV300006_PHPeB",
                                            "plasmid_tars_alias": None,
                                            "prep_lot_number": "VT7354G",
                                            "prep_date": "2024-05-08",
                                            "prep_type": "Purified",
                                            "prep_protocol": "SOP#VC003",
                                        },
                                        "addgene_id": None,
                                        "titer": 4010000000000,
                                        "titer_unit": "gc/mL",
                                    }
                                ],
                                "targeted_structure": None,
                                "relative_position": ["Left"],
                                "dynamics": [
                                    {
                                        "object_type": "Injection dynamics",
                                        "profile": "Bolus",
                                        "volume": 300,
                                        "volume_unit": "nanoliter",
                                        "duration": None,
                                        "duration_unit": None,
                                        "injection_current": None,
                                        "injection_current_unit": None,
                                        "alternating_current": None,
                                    },
                                ],
                                "protocol_id": "dx.doi.org/10.17504/protocols.io.bp2l6nr7kgqe/v4",
                                "coordinate_system_name": "BREGMA_ARID",
                                "coordinates": [
                                    [
                                        {
                                            "object_type": "Translation",
                                            "translation": [
                                                -5.4,
                                                -0.85,
                                                0,
                                                3.2,
                                            ],
                                        },
                                        {
                                            "object_type": "Rotation",
                                            "angles": [0, 0, 0],
                                            "angles_unit": "degrees",
                                        },
                                    ]
                                ],
                            },
                        ],
                        "notes": None,
                    }
                ],
                "specimen_procedures": [],
                "coordinate_system": {
                    "object_type": "Coordinate system",
                    "name": "BREGMA_ARID",
                    "origin": "Bregma",
                    "axes": [
                        {
                            "object_type": "Axis",
                            "name": "AP",
                            "direction": "Posterior_to_anterior",
                        },
                        {
                            "object_type": "Axis",
                            "name": "ML",
                            "direction": "Left_to_right",
                        },
                        {
                            "object_type": "Axis",
                            "name": "SI",
                            "direction": "Superior_to_inferior",
                        },
                        {
                            "object_type": "Axis",
                            "name": "Depth",
                            "direction": "Up_to_down",
                        },
                    ],
                    "axis_unit": "millimeter",
                },
                "notes": None,
            },
        }
    )

    sample_subject = json.dumps(
        {
            "subject": {
                "object_type": "Subject",
                "schema_version": "2.0.12",
                "subject_id": "752014",
                "subject_details": {
                    "object_type": "Mouse subject",
                    "sex": "Male",
                    "date_of_birth": "2024-07-05",
                    "strain": {
                        "name": "C57BL/6J",
                        "species": "Mus musculus",
                        "registry": "Mouse Genome Informatics (MGI)",
                        "registry_identifier": "MGI:3028467",
                    },
                    "species": {
                        "name": "Mus musculus",
                        "common_name": "House mouse",
                        "registry": "National Center for Biotechnology Information (NCBI)",
                        "registry_identifier": "NCBI:txid10090",
                    },
                    "alleles": [],
                    "genotype": "Dbh-Cre-KI/wt",
                    "breeding_info": {
                        "object_type": "Breeding info",
                        "breeding_group": "unknown",
                        "maternal_id": "unknown",
                        "maternal_genotype": "unknown",
                        "paternal_id": "unknown",
                        "paternal_genotype": "unknown",
                    },
                    "wellness_reports": [],
                    "housing": {
                        "object_type": "Housing",
                        "cage_id": "8275812",
                        "room_id": "221",
                        "light_cycle": None,
                        "home_cage_enrichment": [],
                        "cohoused_subjects": [],
                    },
                    "source": {
                        "name": "Allen Institute",
                        "abbreviation": "AI",
                        "registry": "Research Organization Registry (ROR)",
                        "registry_identifier": "03cpe7c52",
                    },
                    "restrictions": None,
                    "rrid": None,
                },
                "notes": None,
            }
        }
    )

    sample_processing = """
{"processing":{
    "piplines": Optional[List[Code]],
    "data_processes": List[DataProcess], -> For processing done with pipelines, list the repositories here. Pipelines must use the name field ,and be referenced in the pipeline_name field of a DataProcess.
    "notes: : Optional[str],
    "dependency_graph": Optional[str] -> Directed graph of processing step dependencies. Each key is a process name, and the value is a list of process names that are inputs to that process.
}}
The following is in a DataProcess class:
    {
    "process_type": ProcessName,
    "name": str,
    "stage": ProcessStage,
    "code": Code,
    "experimenters": List[str],
    "pipeline_name": Optional[str],
    "start_date_time": datetime,
    "end_date_time": datetime,
    "output_path": Optional[AssetPath], -> Path to processing outputs, if stored.
    "output_parameters": dict, -> Output parameters
    "notes": Optional[str],
    "resources": Optional[ResourceUsage]
    }
The following is in a Code class:
{
"url": str, -> URL to code repository
"name": Optional[str],
"version": Optional[str],
"container": Optional[Container],
"run_script": Optional[pathlib.Path], -> Path to run script
"language": Optional[str], -> Programming language used
"language_version": Optional[str], 
"input_data": Optional[List[DataAsset or CombinedData]], -> Input data used in the code or script
"parameters": Optional[dict], -> Parameters used in the code or script
"core_dependency": Optional[Software] -> For code with a core software package dependency, e.g. Bonsai
}

"""
    sample_quality_control = json.dumps(
        {
            "quality_control": {
                "object_type": "Quality control",
                "describedBy": "https://raw.githubusercontent.com/AllenNeuralDynamics/aind-data-schema/main/src/aind_data_schema/core/quality_control.py",
                "schema_version": "2.0.6",
                "metrics": [
                    {
                        "object_type": "QC metric",
                        "name": "Raw data experiment1_Record Node 104#Neuropix-PXI-100.ProbeA_recording1_group0 ",
                        "modality": {
                            "name": "Extracellular electrophysiology",
                            "abbreviation": "ecephys",
                        },
                        "stage": "Raw data",
                        "value": {
                            "value": "",
                            "options": ["Normal", "No spikes", "Noisy"],
                            "status": ["Pass", "Fail", "Fail"],
                            "type": "dropdown",
                        },
                        "status_history": [
                            {
                                "object_type": "QC status",
                                "evaluator": "",
                                "status": "Pending",
                                "timestamp": "2025-06-15 22:43:10.795111+00:00",
                            }
                        ],
                        "description": " ",
                        "reference": " ",
                        "tags": ["Raw Data"],
                        "evaluated_assets": None,
                    }
                ],
            }
        }
    )

    sample_metadata = json.dumps(
        {
            "location": "s3://aind-open-data/SmartSPIM_662616_2023-03-06_17-47-13",
            "name": "SmartSPIM_662616_2023-03-06_17-47-13 ",
            "schema_version": "0.2.7",
        }
    )

    metadata_prompt = f"""
The following dictionaries are examples of how each major class in the metadata is structured in a sample asset.
This is a sample procedures field: {sample_procedures}. In order to access fields, start with 'procedures.<field>, like procedures.subject_procedures.
This is a sample acquisition field: {sample_acquisition}. In order to access fields, start with 'acquisition.<field>, like acquisition.sample_immersion.
This is a sample instrument field: {sample_instrument}. In order to access fields, start with 'instrument.<field>, like instrument.instrument_id.
This is a sample processing field: {sample_processing}. In order to access fields, start with 'processing.<field>, like processing.analyses.
This is a sample data_description field {sample_data_description}. In order to access fields, start with 'data_description.<field>, like data_description.project_name.
This is a sample subject field {sample_subject}. In order to access fields, start with 'subject.<field>, like subject.subject_id.
This is a sample quality control field {sample_quality_control}. In order to access fields, start with 'quality_control.<field>, like quality_control.metrics.

There are several miscellaneous top level fields which are represented here {sample_metadata}.These can just be accessed by the field name.
"""

    schema_prompt = f"""
You are an expert neuroscientist professor who is proficient at constructing mongodb queries based on a user's query. This is the user's query: {query}
Your task is to construct a concise query filter that takes into account all the details the user is looking for
The database you will be working with is a neuroscience metadata database. Follow the instructions below to create queries specific to the type of data found in the database. 
Do not make up fields. It is vital you do not hallucinate.

Note that the session field is used for physiology based modalities like behaviour, optical physiology etc and acquisition is used for modalities like smartspim or exaspim. 
If a question is ambiguous or you are unsure which field the data might exist in, use both fields, do not prioritize one over the other. 

If unsure about the name of a field, use regex and the option i, to be flexible with capitalization. For example, {{data_description.project_name: {{ $regex: "patch foraging", $options: 'i' }}}}

Here are the different modality types:
Access them through data_description.modality.name or data_description.modality.abbreviation
1.                                                                                                                                                              
    abbreviation:  "behavior"
2.
    name: "Behavior videos"
    abbreviation: "behavior -videos"
3.           
    name: "Confocal microscopy"
    abbreviation: "confocal"
4.                                                                                                          
    name: "Electromyography"
    abbreviation: "EMG"                                                                    
5.
name: "Extracellular electrophysiology"
 abbreviation:  "ecephys"
 6.                       
    name: "Fiber photometry"                       
    abbreviation: "fib"
7.                                                  
    name: "Fluorescence micro-optical sectioning tomography"
    abbreviation: "fMOST"
8.
    name: "Intracellular electrophysiology"
    abbreviation: "icephys"
9.
    name:"Intrinsic signal imaging"
    abbreviation:"ISI"
10.
    name:"Magnetic resonance imaging"
    abbreviation:  "MRI"
11.

    name:  "Multiplexed error-robust fluorescence in situ hybridization"
    abbreviation: "merfish"
12.
    name: "Planar optical physiology"
    abbreviation: "pophys"

13.
    name: "Scanned line projection imaging"
    abbreviation:  "slap"

14.
    name:  "Selective plane illumination microscopy"
    abbreviation: "SPIM"


Ensure that the fields you determine are best for answering the question actually exist. 
Do not pass along information that's False or non existent. It is crucial you follow this step.

"""

    examples = """

Here are some example queries and their filters:
1.
Question: "Retrieve records for subject 740955"
Answer: {'subject.subject_id':'740955'}
2.
Question: "Retrieve records for subjects with genotype 'Sert-Cre/wt' in the project titled:
Discovery-Neuromodulator circuit dynamics during foraging - Subproject 1 Electrophysiological Recordings from NM Neurons During Behavior" 
Answer: {'subject.subject_details.genotype':'Sert-Cre/wt', "data_description.project_name":"
Discovery-Neuromodulator circuit dynamics during foraging - Subproject 1 Electrophysiological Recordings from NM Neurons During Behavior"}
3. 
Question: "Retrieve records for subject x where qc evaluations for behaviour passed"
Answer: {"subject.subject_id": "792288","quality_control.metrics": { $elemMatch: { "modality.name": "Behavior", "latest_status": "Pass"} }}
4.
Question: Retrieve records from the openscope project where the session type is OPHYS_9_moving_texture.
Answer: 
 { "data_description.project_name": "OpenScope","acquisition.acquisition_type": "OPHYS_9_moving_texture"}
"""

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{schema_prompt}",
                },
                {
                    "type": "text",
                    "text": f"{metadata_prompt}",
                },
                {
                    "type": "text",
                    "text": f"{examples}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return messages
