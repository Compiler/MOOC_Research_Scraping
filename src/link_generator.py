
period = [str(1622530800000), str(1622531000000)]
increment = 10000
link_count = 100
for i in range(link_count):
    link = "https://studio.youtube.com/channel/UCfdfhDEwT_KzyBhWmmL23IQ/analytics/tab-overview/period-default/explore?c=UCfdfhDEwT_KzyBhWmmL23IQ&entity_type=VIDEO&entity_id=Xmc7y2crluY&time_period=" + period[0] + "%2C" + period[1] + "&explore_type=TABLE_AND_CHART&metric=VIEWS&comparison_metric=WATCH_TIME&granularity=DAY&t_metrics=WATCH_TIME&t_metrics=VIEWS&t_metrics=AVERAGE_WATCH_TIME&t_metrics=AVERAGE_WATCH_PERCENTAGE&dimension=VIDEO&o_column=VIEWS&o_direction=ANALYTICS_ORDER_DIRECTION_DESC"
    print(link)
    period[1] = str((int)(period[1]) + increment)
#172800000