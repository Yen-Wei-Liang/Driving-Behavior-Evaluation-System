import unittest
import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
from scipy.signal import get_window
from scipy.fftpack import fft
from scipy.signal import stft
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from filterpy.kalman import KalmanFilter
from tqdm import tqdm
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class NoiseFilter:

    def Introduction(self):
        """
        Function: Introduction to how to use this class and its methods.

        Note: This function will print out the guide to console.
        """
        intro = """
         .----------------.  .----------------.  .----------------.  .----------------.   
        | .--------------. || .--------------. || .--------------. || .--------------. |  
        | |     _____    | || |  _________   | || |  _______     | || |     _____    | |  
        | |    |_   _|   | || | |  _   _  |  | || | |_   __ \    | || |    |_   _|   | |  
        | |      | |     | || | |_/ | | \_|  | || |   | |__) |   | || |      | |     | |  
        | |      | |     | || |     | |      | || |   |  __ /    | || |      | |     | |  
        | |     _| |_    | || |    _| |_     | || |  _| |  \ \_  | || |     _| |_    | |  
        | |    |_____|   | || |   |_____|    | || | |____| |___| | || |    |_____|   | |  
        | |              | || |              | || |              | || |              | |  
        | '--------------' || '--------------' || '--------------' || '--------------' |  
         '----------------'  '----------------'  '----------------'  '----------------'   
         .----------------.  .----------------.  .----------------.  .----------------.   
        | .--------------. || .--------------. || .--------------. || .--------------. |  
        | | ____    ____ | || |     __       | || |     ____     | || |     ____     | |  
        | ||_   \  /   _|| || |    /  |      | || |   .'    '.   | || |   .'    '.   | |  
        | |  |   \/   |  | || |    `| |      | || |  |  .--.  |  | || |  |  .--.  |  | |  
        | |  | |\  /| |  | || |     | |      | || |  | |    | |  | || |  | |    | |  | |  
        | | _| |_\/_| |_ | || |    _| |_     | || |  |  `--'  |  | || |  |  `--'  |  | |  
        | ||_____||_____|| || |   |_____|    | || |   '.____.'   | || |   '.____.'   | |  
        | |              | || |              | || |              | || |              | |  
        | '--------------' || '--------------' || '--------------' || '--------------' |  
         '----------------'  '----------------'  '----------------'  '----------------'   
 
        歡迎使用 NoiseFilter 功能！
        
        這個Class包含以下功能：
        
        1. filter_and_denoise: 應用低通、高通或帶通濾波器以去除噪音。
           用法: filter_and_denoise(self, signal, fs, save_plot=False, filter_type='low')
        2. apply_window: 應用窗函式濾波器以去除噪音。
           用法: apply_window(data, selected_window='hamming')
        3. apply_kalman_filter: 應用卡爾曼濾波器去除噪音。
           用法: apply_kalman_filter(self, dataset, features, q_noise=0.0001, r_noise=0.001):
        """
        print(intro)

    
    def __init__(self):
        self.half_fs = None


    #################################### filter_and_denoise 功能模塊 Start ####################################

    # 濾波器副程式    
    def butter_filter(self, signal, cutoff, fs, order=4, btype='low'):
        if self.half_fs is None or self.half_fs != 0.5 * fs:
            self.half_fs = 0.5 * fs
        b, a = butter(order, np.array(cutoff) / self.half_fs, btype=btype)
        return filtfilt(b, a, signal)
    
    # 濾波器副程式
    def plot_signal(self, subplot_idx, title, t, signal):
        plt.subplot(4, 1, subplot_idx)
        plt.title(title)
        plt.plot(t, signal)
    
    # 濾波器副程式
    def select_filter_output(self, filter_type, y_low, y_high, y_band):
        if filter_type == 'low':
            return y_low
        elif filter_type == 'high':
            return y_high
        elif filter_type == 'band':
            return y_band
        
    # 高/低/帶通濾波器主程式
    def filter_and_denoise(self, signal, fs, save_plot=False, filter_type=None):
        T = 1.0/fs
        t = np.arange(0, 1, T)

        self.plot_signal(1, "Original Signal", t, signal)
        
        y_low = self.butter_filter(signal, 70, fs, btype='low')
        self.plot_signal(2, "Low-pass Filter", t, y_low)

        y_high = self.butter_filter(signal, 70, fs, btype='high')
        self.plot_signal(3, "High-pass Filter", t, y_high)
        
        y_band = self.butter_filter(signal, [70, 130], fs, btype='band')
        self.plot_signal(4, "Band-pass Filter", t, y_band)

        plt.tight_layout()
        
        if save_plot:
            plt.savefig('filter_and_denoise_plot.png')
        
        plt.show()

        return self.select_filter_output(filter_type, y_low, y_high, y_band)

    # 窗函式濾波主程式
    def apply_window(self, data, selected_window='hamming'):

        # All available windows
        all_windows = ['boxcar', 'triang', 'blackman', 'hamming', 'hann', 'bartlett', 'flattop', 'parzen', 'bohman', 'blackmanharris', 'nuttall', 'barthann', 'cosine', 'exponential', 'tukey', 'taylor', 'lanczos']
    
        # Plot all windows if show_all is True
        plt.figure(figsize=(15, 15))
        for i, w_type in enumerate(all_windows):
            plt.subplot(6, 3, i+1)
            windowed_data = data * get_window(w_type, len(data))
            plt.title(f'{w_type.capitalize()}')
            plt.plot(windowed_data)
        
            if w_type == selected_window:
                selected_windowed_data = windowed_data  # Store the selected windowed data
            
        plt.tight_layout(pad=2.0)
        plt.show()
    
        return selected_windowed_data  # Return the selected windowed data

     # 卡爾曼濾波器副程式
    def initialize_kalman_filter(self, dim, q_noise=0.0001, r_noise=0.001):
        """Initializes a Kalman filter."""
    
        kf = KalmanFilter(dim_x=dim, dim_z=dim)
        kf.F = np.eye(dim)
        kf.H = np.eye(dim)
        kf.Q = np.eye(dim) * q_noise
        kf.R = np.eye(dim) * r_noise
        kf.x = np.zeros((dim, 1))
        kf.P = np.eye(dim)

        return kf

    # 卡爾曼濾波器主程式
    def apply_kalman_filter(self, dataset, features, q_noise=0.0001, r_noise=0.001):
        """
        Apply Kalman filter to a dataset.

        Parameters:
            dataset: DataFrame containing the data.
            features: Features to apply the filter on.
            q_noise: Noise in the system.
            r_noise: Measurement noise.
            save_path: Path of the CSV file to save the filtered data.
        """
    
        # Initialize the Kalman filter
        kf = self.initialize_kalman_filter(len(features), q_noise, r_noise)

        # Convert DataFrame to numpy array for efficiency
        data_array = dataset[features].to_numpy()
        filtered_data_array = np.zeros_like(data_array)

        # Apply the Kalman filter
        for i in tqdm(range(data_array.shape[0])):
            measurement = data_array[i, :].reshape(-1, 1)

            # Predict the next state
            kf.predict()

            # Update the state
            kf.update(measurement)

            # Save the filtered result
            filtered_data_array[i, :] = kf.x[:, 0]

        # Convert the filtered data back to DataFrame and update the original dataset
        filtered_df = pd.DataFrame(filtered_data_array, columns=features)
        for feature in features:
            dataset[feature] = filtered_df[feature]

        return dataset



class SignalModel:
    pass

class TraditionalFFTModel(SignalModel):

    def Introduction(self):
        """
        Function: Introduction to how to use this class and its methods.

        Note: This function will print out the guide to console.
        """
        intro = """
         .----------------.  .----------------.  .----------------.  .----------------.   
        | .--------------. || .--------------. || .--------------. || .--------------. |  
        | |     _____    | || |  _________   | || |  _______     | || |     _____    | |  
        | |    |_   _|   | || | |  _   _  |  | || | |_   __ \    | || |    |_   _|   | |  
        | |      | |     | || | |_/ | | \_|  | || |   | |__) |   | || |      | |     | |  
        | |      | |     | || |     | |      | || |   |  __ /    | || |      | |     | |  
        | |     _| |_    | || |    _| |_     | || |  _| |  \ \_  | || |     _| |_    | |  
        | |    |_____|   | || |   |_____|    | || | |____| |___| | || |    |_____|   | |  
        | |              | || |              | || |              | || |              | |  
        | '--------------' || '--------------' || '--------------' || '--------------' |  
         '----------------'  '----------------'  '----------------'  '----------------'   
         .----------------.  .----------------.  .----------------.  .----------------.   
        | .--------------. || .--------------. || .--------------. || .--------------. |  
        | | ____    ____ | || |     __       | || |     ____     | || |     ____     | |  
        | ||_   \  /   _|| || |    /  |      | || |   .'    '.   | || |   .'    '.   | |  
        | |  |   \/   |  | || |    `| |      | || |  |  .--.  |  | || |  |  .--.  |  | |  
        | |  | |\  /| |  | || |     | |      | || |  | |    | |  | || |  | |    | |  | |  
        | | _| |_\/_| |_ | || |    _| |_     | || |  |  `--'  |  | || |  |  `--'  |  | |  
        | ||_____||_____|| || |   |_____|    | || |   '.____.'   | || |   '.____.'   | |  
        | |              | || |              | || |              | || |              | |  
        | '--------------' || '--------------' || '--------------' || '--------------' |  
         '----------------'  '----------------'  '----------------'  '----------------'   
 
        歡迎使用 TraditionalFFTModel 功能！
        
        這個Class包含以下功能：
        
        1. check_anomalies: 檢查異常狀況(判斷主頻率+-10%是否高於平均值)
           用法: check_anomalies(signal, sampling_rate):
           
        """


    def perform_fft(self, signal, sampling_rate):
        n = len(signal)
        freq = np.fft.fftfreq(n, 1/sampling_rate)
        fft_values = np.fft.fft(signal)
        return freq, fft_values

    def find_main_frequency(self, freq, fft_values):
        positive_freq_idx = np.where(freq > 0)
        freq = freq[positive_freq_idx]
        fft_values = fft_values[positive_freq_idx]
        
        magnitude = np.abs(fft_values)
        main_freq_index = np.argmax(magnitude)
        main_freq = freq[main_freq_index]
        return main_freq


    def check_anomalies(self, signal, sampling_rate):
        freq, fft_values = self.perform_fft(signal, sampling_rate)
        main_freq = self.find_main_frequency(freq, fft_values)

        print("Main frequency is:", main_freq)

        magnitude = np.abs(fft_values)
        avg_magnitude = np.mean(magnitude)
    
        # 設定頻率範圍
        tolerance = 0.1
        second_harmonic_range = [2 * main_freq * (1 - tolerance), 2 * main_freq * (1 + tolerance)]
        third_harmonic_range = [3 * main_freq * (1 - tolerance), 3 * main_freq * (1 + tolerance)]

        # 找到範圍內的頻率
        second_harmonic_indices = np.where((freq >= second_harmonic_range[0]) & (freq <= second_harmonic_range[1]))
        third_harmonic_indices = np.where((freq >= third_harmonic_range[0]) & (freq <= third_harmonic_range[1]))

        # 檢查範圍內的最大幅度
        second_harmonic_magnitude = np.max(magnitude[second_harmonic_indices])
        third_harmonic_magnitude = np.max(magnitude[third_harmonic_indices])

        if second_harmonic_magnitude > avg_magnitude:
            print("異常狀況: 不平衡")
        elif third_harmonic_magnitude > avg_magnitude:
            print("異常狀況: 彎曲變形")
        else:
            print("異常狀況: None")


        positive_freq_idx = np.where(freq > 0)
        freq = freq[positive_freq_idx]
        fft_values = fft_values[positive_freq_idx]
        
        plt.figure()
        plt.title("Frequency Spectrum")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.plot(freq, np.abs(fft_values))
        
        for i in [1, 2, 3]:
            plt.axvline(x=i*main_freq, color='r', linestyle='--')
        
        plt.show()
 

# 模擬一個訊號
# t = np.linspace(0, 1, 500, endpoint=False)
# signal = np.cos(2 * np.pi * 7 * t) + np.sin(2 * np.pi * 13 * t)



# 使用SignalAnalyzer類
# analyzer = SignalAnalyzer()
# analyzer.check_anomalies(signal, 500)






class SignalModel:
    # 共同的方法和屬性
    pass



class SimpleAIModel(SignalModel):
    # 簡單AI特有的方法和屬性
    pass

class ComplexAIModel(SignalModel):
    # 複雜AI特有的方法和屬性
    pass













#####################################  資料正規化  start #################################################

    def normalize_data(self, dataset, feature, method="minmax", save_path=None):
        """
        Function: Normalize specified feature in dataset.

        Parameters:
            dataset: The dataframe containing the data to normalize.
            feature: The column(s) in the dataframe to normalize.
            method: The normalization method to use. Options are "minmax", "standard", "robust".
            save_path: Path to save normalized data. If None, data will not be saved.

        Returns:
            normalized_df: The dataframe after normalization.
        """

        # 定義一個字典來映射方法名稱到相應的類
        methods = {
            "minmax": MinMaxScaler,
            "standard": StandardScaler,
            "robust": RobustScaler
        }

        # 檢查指定的方法是否存在
        if method not in methods:
            raise ValueError(f"Invalid method. Expected one of: {list(methods.keys())}")

        # 創建相應的物件
        scaler = methods[method]()

        # 對指定特徵進行正規化
        normalized_data = scaler.fit_transform(dataset[feature])

        # 將正規化後的資料轉換為DataFrame
        normalized_df = pd.DataFrame(normalized_data, columns=feature)

        return normalized_df


########################################################################################################




if __name__ == '__main__':
    unittest.main()











def fft_fcn_signal_model(signal, model_path=None):
    # FFT 轉換
    fft_values = np.fft.fft(signal)
    magnitude = np.abs(fft_values)
    
    # 數據預處理（例如，正規化）
    magnitude = magnitude / np.max(magnitude)
    
    # 如果提供了模型路徑，則載入模型
    if model_path:
        model = load_model(model_path)
        prediction = model.predict(magnitude.reshape(1, -1))
        return "正常" if np.argmax(prediction) == 0 else "異常"
    
    # 否則，訓練一個新模型
    else:
        # 假設 labels 是一個與 signal 長度相同的標籤數組
        # 0 表示正常，1 表示異常
        labels = np.random.randint(0, 2, 1)  # 這裡只生成一個標籤，與單個訊號對應
        
        # 建立模型
        model = Sequential([
            Dense(128, activation='relu', input_shape=(len(magnitude),)),
            Dense(64, activation='relu'),
            Dense(32, activation='relu'),
            Dense(16, activation='relu'),
            Dense(2, activation='softmax')
        ])
        
        # 編譯模型
        model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        
        # 訓練模型
        model.fit(magnitude.reshape(1, -1), labels, epochs=10)  # 這裡也只有一個訓練樣本
        
        # 儲存模型（如果需要）
        model.save("my_model.h5")
        
        return "模型訓練完成，已儲存為 'my_model.h5'"
    

# 模擬一個訊號
# signal = np.sin(2 * np.pi * np.linspace(0, 1, 100))

# 訓練模型
# print(fft_fcn_signal_model(signal))

# 使用預訓練的模型進行預測
# print(fft_fcn_signal_model(signal, model_path="my_model.h5"))