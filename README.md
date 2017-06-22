# kNN-in-python

import csvimport randomimport mathimport operatordef load_dataset(filename, split, training_set=[], test_set=[]):    with open(filename, 'rb') as csvfile:        lines = csv.reader(csvfile)        dataset = list(lines)        for x in range(len(dataset)-1):            for y in range(6):                dataset[x][y] = float(dataset[x][y])            if random.random() < split:                training_set.append(dataset[x])            else:                test_set.append(dataset[x])def format_dataset(filename):    with open(filename,'rb') as csvfile:        reader = csv.reader(csvfile)        new_dataset = open('carsvalue.csv', "wb")        writer = csv.writer(new_dataset)        for row in reader:            new_row = [None] * 7            # Buying cost representation            if repr(row[0]) == "'vhigh'":                new_row[0] = '3.0'            elif repr(row[0]) == "'high'":                new_row[0] = '2.0'            elif repr(row[0]) == "'med'":                new_row[0] = '1.0'            elif repr(row[0]) == "'low'":                new_row[0] = '0.0'            # Maintenance cost representation            if repr(row[1]) == "'vhigh'":                new_row[1] = '3.0'            elif repr(row[1]) == "'high'":                new_row[1] = '2.0'            elif repr(row[1]) == "'med'":                new_row[1] = '1.0'            elif repr(row[1]) == "'low'":                new_row[1] = '0.0'            # Doors representation            if repr(row[2]) == "'5more'":                new_row[2] = '3.0'            elif repr(row[2]) == "'4'":                new_row[2] = '2.0'            elif repr(row[2]) == "'3'":                new_row[2] = '1.0'            elif repr(row[2]) == "'2'":                new_row[2] = '0.0'            # Capacity representaion            if repr(row[3]) == "'more'":                new_row[3] = '2.0'            elif repr(row[3]) == "'4'":                new_row[3] = '1.0'            elif repr(row[3]) == "'2'":                new_row[3] = '0.0'            # Trunk Size representaion            if repr(row[4]) == "'big'":                new_row[4] = '2.0'            elif repr(row[4]) == "'med'":                new_row[4] = '1.0'            elif repr(row[4]) == "'small'":                new_row[4] = '0.0'            # Safety representaion            if repr(row[5]) == "'high'":                new_row[5] = '2.0'            elif repr(row[5]) == "'med'":                new_row[5] = '1.0'            elif repr(row[5]) == "'low'":                new_row[5] = '0.0'            new_row[6] = row[6]                            #print(repr(new_row))            writer.writerow(new_row)            #now we write new_row to csv filedef euclid_distance(instance1, instance2, length):    distance = 0    for x in range(length):        distance += pow((instance1[x] - instance2[x]), 2)    return math.sqrt(distance)def get_neighbors(training_set, test_instance, k):    distances = []    length = len(test_instance) - 1    for x in range(len(training_set)):        dist = euclid_distance(test_instance, training_set[x], length)        distances.append((training_set[x], dist))    distances.sort(key=operator.itemgetter(1))    neighbors = []    for x in range(k):        neighbors.append(distances[x][0])    return neighborsdef get_response(neighbors):    class_votes = {}    for x in range(len(neighbors)):        response = neighbors[x][-1]        if response in class_votes:            class_votes[response] += 1        else:            class_votes[response] = 1    sorted_votes = sorted(class_votes.iteritems(), key=operator.itemgetter(1), reverse=True)    return sorted_votes[0][0]def get_accuracy(testSet, predictions):   correct = 0   for x in range(len(testSet)):      if testSet[x][-1] == predictions[x]:         correct += 1   return (correct/float(len(testSet))) * 100.0def main():    # sanitize data    training_set = []    test_set = []    split = 0.67    format_dataset('car.data')    load_dataset('carsvalue.csv', split, training_set, test_set)    print 'Train set: ' + repr(len(training_set))    print 'Test set: ' + repr(len(test_set))    # generate predictions    predictions = []    k = 3    for x in range(len(test_set)):        neighbors = get_neighbors(training_set, test_set[x], k)        result = get_response(neighbors)        predictions.append(result)        if repr(result) == repr(test_set[x][-1]):            print ('> predicted = ' + repr(result) + ', actual= ' + repr(test_set[x][-1]))        else:            print ('> predicted = ' + repr(result) + ', actual= ' + repr(test_set[x][-1]) + '    (WRONG)')    accuracy = get_accuracy(test_set, predictions)    print('Accuracy = ' + repr(accuracy) + '%')main()