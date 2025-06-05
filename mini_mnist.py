from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def mini_mnist():
    # 데이터 로드
    digits = load_digits()
    X, y = digits.data, digits.target

    # 정규화 (0-16 -> 0-1)
    X = X / 16.0

    # 원-핫 인코딩
    y_onehot = np.eye(10)[y]

    # 훈련/테스트 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_onehot, test_size=0.2, random_state=42
    )

    print("미니 mnist 과제")
    print(f"훈련 데이터: {X_train.shape}") 
    print(f"테스트 데이터: {X_test.shape}") 
    print("클래스 수: 10개 (0-9 숫자)")

    # TODO: 다중 클래스 분류 신경망 구현
    # 1. 입력층: 64개 (8x8 이미지)
    # 2. 은닉층: 적절한 크기
    # 3. 출력층: 10개 (0-9 숫자)
    # 4. Softmax 활성화 함수
    # 5. Cross-Entropy 손실 함수

    class DigitClassfier:
        def __init__(self,input_size=64,hidden_size=32,output_size=10,learning_rate=0.1):
            self.lr = learning_rate
            self.w1 = np.random.randn(input_size,hidden_size) * 0.01
            self.b1 = np.zeros((1,hidden_size))
            self.w2 = np.random.randn(hidden_size,output_size) * 0.01
            self.b2 = np.zeros((1,output_size))

            # self.z1 = None
            # self.a1 = None
            # self.z2 = None
            # self.a2 = None
        
        #은닉층에는 relu사용
        def relu(self, z):
            return np.maximum(0,z)
        
        def relu_derivative(self, z):
            return (z>0).astype(float)

        def softmax(self,z):
            exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
            return exp_z / np.sum(exp_z, axis=1, keepdims=True)

        def cross_entropy_loss(self,y_pred,y_true):
            epsilon = 1e-12
            y_pred = np.clip(y_pred, epsilon, 1. - epsilon)
            N = y_pred.shape[0]
            loss = -np.sum(y_true * np.log(y_pred + epsilon)) / N
            return loss

        def forward(self,X):
            self.z1 = np.dot(X,self.w1) + self.b1
            self.a1 = self.relu(self.z1)
            self.z2 = np.dot(self.a1,self.w2) + self.b2
            self.a2 = self.softmax(self.z2)

            return self.a2

        def backward(self,X,y):
            m = X.shape[0]

            dz2 = self.a2 - y
            dw2 = (1/m) * np.dot(self.a1.T, dz2)
            db2 = (1/m) * np.sum(dz2,axis=0,keepdims=True)

            dz1 = np.dot(dz2,self.w2.T) * self.relu_derivative(self.z1)
            dw1 = (1/m) * np.dot(X.T, dz1)
            db1 = (1/m) * np.sum(dz1,axis=0,keepdims=True)

            # 가중치 업데이트
            self.w2 -= self.lr * dw2
            self.b2 -= self.lr * db2
            self.w1 -= self.lr * dw1
            self.b1 -= self.lr * db1
        
        #각 입력x에 대해 가장 확률 높은 번호 예측측
        def predict(self,X):
            probs = self.forward(X)
            
            return np.argmax(probs,axis=1)
        
        def accuracy(self,X,y):
            y_pred = self.predict(X)
            y_true_labels = np.argmax(y, axis=1)
            
            return np.mean(y_pred == y_true_labels) #true/false 배열의 true 비율
    
    #모델 학습 및 평가
    model = DigitClassfier()
    epochs = 1000

    for epoch in range(epochs):
        y_pred = model.forward(X_train) #순전파 예측값 계산산
        loss = model.cross_entropy_loss(y_pred,y_train)
        model.backward(X_train,y_train) #역전파로 가중치 업데이트

        if epoch % 100 == 0:
            acc = model.accuracy(X_test,y_test)
            print(f"[Epoch {epoch}] Loss: {loss:.4f}, Accuracy: {acc:.4f}")
    
    print("최종 테스트 정확도:", model.accuracy(X_test, y_test))

mini_mnist()


