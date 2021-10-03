(env-apiclient) PS {path}\client> python -m app.prep_data
(env-apiclient) PS {path}\client> python -m app.main     
Prepare requests: 0:00:00.680105
Requests-responses: 0:00:10.244659
Save responses: 0:00:00.021846
(env-apiclient) PS {path}\client> python -m app.view_results
         ID  default_payment_next_month  score  probability_0  probability_1  log_probability_0  log_probability_1
3019  28020                           0    1.0            1.0            0.0                0.0      -1.741244e+08
3696  28697                           0    1.0            1.0            0.0                0.0      -9.500102e+09
1110  26111                           0    1.0            1.0            0.0                0.0      -1.146796e+09
3159  28160                           0    1.0            1.0            0.0                0.0      -2.802693e+11
4148  29149                           0    1.0            1.0            0.0                0.0      -2.322458e+10
(env-apiclient) PS {path}\client> 