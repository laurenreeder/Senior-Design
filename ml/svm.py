from __future__ import division
from sklearn.svm import SVC
from generate_features import *


def train_classifier(X, y):
	clf = SVC(C=100.0
			  )
	clf.fit(X, y)
	return clf

def train_with_image_dirs(test_dirs, labels):
	if len(labels) != len(test_dirs):
		raise ValueError("Different number of image categories than labels for classification")
	# Get feature vectors for each directory
 	X = [featureVectorsFromDirectory(test_dir) for test_dir in test_dirs]
 	y = []
 	# Add a label to label array for each image
 	for i, label in enumerate(labels):
 		y += [str(label)] * len(X[i])
 	# get all the feature vectors into a single array for the classifier
 	X = [x for feature_list in X for x in feature_list]
 	clf = train_classifier(X, y)
 	return clf

def get_features(image_paths):
	return [getHOGInfo(image_file) for image_file in image_paths]


def train_with_images(image_paths, labels):
    X = get_features(image_paths)
    clf = train_classifier(X, labels)
    return clf

def test_with_images(clf, image_paths, labels):
	X = [getHOGInfo(image_file) for image_file in image_paths]
	predictions = clf.predict(X)
	count = 0
	correct_count = 0
	for label, predicted_label in zip(labels, predictions):
		if label == predicted_label:
			correct_count += 1
		count += 1
	return correct_count / count

def test():
	svc = train_with_images(["/Users/ella/Documents/cis400/101_ObjectCategories/bonsai",
					"/Users/ella/Documents/cis400/101_ObjectCategories/crocodile_head"],
					 ["bonsai", "croc"])
	X_test = fv("/Users/ella/Documents/cis400/101_ObjectCategories/crocodile_head")
	print svc.predict(X_test)

