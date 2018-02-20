
import os
import sys
import twitter_main as tm
import driver as d
import twitterutils as tu

# # Create config dictionary
cf_dict = d.config_init("config.yaml");

# Authorize twitter
twitter = tu.create_twitter_auth(cf_dict)

# Create dictionary of names
all_users = d.get_all_users_from_file(cf_dict)

# task1 = PythonOperator(
#               task_id='get_profiles',
#               python_callable=d.create_profile_stats,
#               op_args=(twitter, cf_dict, all_users),
#               dag=dag_profiles)
#
# task2 = PythonOperator(
#               task_id='create_timelines',
#               python_callable=d.create_timelines,
#               op_args=(twitter, cf_dict, all_users),
#               dag=dag_timelines)
