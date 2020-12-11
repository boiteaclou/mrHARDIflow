# Configuration file for Magic Monkey.

c = get_config()

# -----------------------------------------------------------------------------
# AntsRegistration(MagicMonkeyBaseApplication) configuration
# -----------------------------------------------------------------------------

# Application traits configuration

c.AntsRegistration.log_datefmt = "%Y-%m-%d %H:%M:%S"

c.AntsRegistration.log_format = "[%(name)s]%(highlevel)s %(message)s"

c.AntsRegistration.log_level = 30

c.AntsRegistration.base_config_file = ""


# -----------------------------------------------------------------------------
# AntsConfiguration(MagicMonkeyConfigurable) configuration
# -----------------------------------------------------------------------------

c.AntsConfiguration.accross_modalities = False

c.AntsConfiguration.dimension = 3

c.AntsConfiguration.init_transform = [0, 0, 0]

c.AntsConfiguration.inlier_range = [0.005, 0.995]

c.AntsConfiguration.interpolation = "Linear"

c.AntsConfiguration.klass = "magic_monkey.config.ants.AntsConfiguration"

c.AntsConfiguration.match_histogram = True

c.AntsConfiguration.passes = [{
    "conv_eps": 1e-6,
    "conv_max_iter": [200, 100, 50, 25],
    "conv_win": 10,
    "grad_step": 0.1,
    "klass": "magic_monkey.traits.ants.AntsRigid",
    "metrics": [
        {
            "target_index": 0,
            "moving_index": 0,
            "args": [
                1.0,
                64,
                "Regular",
                0.5
            ],
            "klass": "magic_monkey.traits.ants.MetricMI"
        }
    ],
    "shrinks": [
        8,
        4,
        2,
        1
    ],
    "smoothing": [
        3,
        2,
        1,
        0
    ]
}, {
    "conv_eps": 1e-6,
    "conv_max_iter": [200, 100, 50, 25],
    "conv_win": 10,
    "grad_step": 0.1,
    "klass": "magic_monkey.traits.ants.AntsAffine",
    "metrics": [
        {
            "target_index": 0,
            "moving_index": 0,
            "args": [
                1.0,
                64,
                "Regular",
                0.5
            ],
            "klass": "magic_monkey.traits.ants.MetricMI"
        }
    ],
    "shrinks": [
        8,
        4,
        2,
        1
    ],
    "smoothing": [
        3,
        2,
        1,
        0
    ]
}, {
    "conv_eps": 1e-06,
    "conv_max_iter": [50, 25, 10],
    "conv_win": 10,
    "grad_step": 0.1,
    "var_penality": 3,
    "var_total": 0,
    "klass": "magic_monkey.traits.ants.AntsSyN",
    "metrics": [
        {
            "target_index": 0,
            "moving_index": 0,
            "args": [
                1.0,
                32,
                "Regular",
                0.25
            ],
            "klass": "magic_monkey.traits.ants.MetricMI"
        }
    ],
    "shrinks": [
        4,
        2,
        1
    ],
    "smoothing": [
        3,
        2,
        1
    ]
}]

c.AntsConfiguration.use_float = False
