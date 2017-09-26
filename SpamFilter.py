from textblob.classifiers import NaiveBayesClassifier
import sys

reload(sys)
sys.setdefaultencoding('utf8')

with open('hamlinks.txt') as f:
    ham = f.readlines()

# Strip off \n
ham = [x.strip() for x in ham]
# Get rid of ascii errors
ham = [x.decode("ascii", errors="ignore").encode() for x in ham]

ham_links = []

#identify these as negative spam
for i in ham:
    ham_links.append((i,"neg"))

#print ham_links

with open('badLinks.txt') as y:
    spam = y.readlines()

spam = [r.strip() for r in spam]

spam_links = []

#identify these as positive spam
# list of tuples
for j in spam:
    spam_links.append((j,"pos"))

#print spam_links

# Combine the two lists
train_links = ham_links + spam_links

# create classifier
cl = NaiveBayesClassifier(train_links)
#test = "D.C. court rules tracking phones without a warrant is unconstitutional"

#res = cl.classify(test)
#print "The text is Spam: ", res

with open('twitter_links.txt') as f:
    test_data = f.readlines()

# Strip off \n
test_data = [x.strip() for x in test_data]
# Get rid of ascii errors
test_data = [x.decode("ascii", errors="ignore").encode() for x in test_data]

for i in test_data:
#    print i
    #res = cl.classify(i)
    prob = cl.prob_classify(i)
    res = round(prob.prob("pos"),2)
    res = res * 100
    if res >= 50:
        print "SPAM: ", i
        print res



#res_prob = cl.prob_classify(test)

#print "Percentage of pos result: ", round(res_prob.prob("pos"), 2)
#print "Percentage of neg result: ", round(res_prob.prob("neg"), 2)

#print cl.show_informative_features(5)



