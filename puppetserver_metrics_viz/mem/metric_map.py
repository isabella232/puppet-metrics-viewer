from puppetserver_metrics_viz.mem.metric import MemoryMetric

# TODO: combine this class with MemoryMetric, this isn't useful

class MemoryMetricMap:
    def __init__(self, timestamp, json_data):
        self.timestamp = timestamp
        self.jvm_metrics = MemoryMetric(json_data)
        # # TODO: this map probably isn't actually useful for anything,
        # # originally copied from the HTTP metrics.
        # # this whole class should potentially just be a list/collection
        # # data structure rather than a map.
        # self.metric_map = {}
        # for metric in self.jvm_metrics:
        #     self.metric_map[timestamp] = metric
