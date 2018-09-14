import multiprocessing
from vehicle_counter import VehicleCounter
import numpy as np

def wrapper(video_path, city_name, location_name, minm_area, roi):
		
	# vo = TrafficCongestion(video_path, city_name, location_name)
	# vo.congestion(video_path, minm_area=minm_area,roi=roi,plot_intermediate=False)

	vo = VehicleCounter(video_path, city_name, location_name)
	vo.vehicle_counter(minm_area=minm_area, roi=roi, plot_intermediate=True, check_interval=10, 
	method='quantile', aggregation_time='3T', congestion_threshold=0.20)


# video_path = '/media/anuj/Work-HDD/WORK/CLOUD-DRIVE/Google-Drive/Computer-Vision/Sample-Videos/Car-Analytics/vijaywada_5min.mp4'
# roi = np.array([(532, 256), (953, 307), (849, 808), (52, 541)],dtype = np.float32)
# minm_area = 13455




video_channel_test_arr = ['/media/anuj/Work-HDD/WORK/CLOUD-DRIVE/Google-Drive/Computer-Vision/Sample-Videos/Car-Analytics/vijaywada_5min.mp4', '/media/anuj/Work-HDD/WORK/CLOUD-DRIVE/Google-Drive/Computer-Vision/Sample-Videos/Car-Analytics/vijaywada_5min.mp4']
location_name_test_arr = ['akashwani_east', 'data_center']
minm_area_test_arr = [13455, 13455]
roi_test_arr = [[(532, 256), (953, 307), (849, 808), (52, 541)], [(532, 256), (953, 307), (849, 808), (52, 541)]]

if __name__ == '__main__':
	
	jobs = []
	for i in range(len(minm_area_test_arr)):
		video_path = video_channel_test_arr[i]
		location_name = location_name_test_arr[i]
		minm_area = minm_area_test_arr[i]
		roi = np.array(roi_test_arr[i], dtype = np.float32)

		p = multiprocessing.Process(target=wrapper, args=(video_path, 'hyderabad', location_name, minm_area, roi,))
		jobs.append(p)
		p.start()