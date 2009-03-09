# From http://members.unine.ch/jacques.savoy/clef/englishST.txt

STOPWORDS = set(['secondly', 'all', 'consider', 'whoever', 'four', 'edu', 'go', 'causes', 'seemed', 'rd', 'certainly', 'vs', 'to', 'asking', 'th', 'under', 'sorry', "a's", 'sent', 'far', 'every', 'yourselves', "we'll", 'went', 'did', 'forth', "they've", 'try', 'p', "it'll", "i'll", 'says', "you'd", 'yourself', 'likely', 'further', 'quite', 'even', 'what', 'appear', 'brief', 'goes', 'sup', 'new', 'ever', "c'mon", 'whose', 'respectively', 'never', 'let', 'others', "hadn't", 'along', "aren't", 'k', 'allows', "i'd", 'howbeit', 'usually', 'whereupon', "i'm", 'changes', 'thats', 'hither', 'via', 'followed', 'merely', 'while', 'viz', 'everybody', 'use', 'from', 'would', 'contains', 'two', 'next', 'few', 'therefore', 'taken', 'themselves', 'thru', 'tell', 'more', 'knows', 'becomes', 'hereby', 'herein', "ain't", 'particular', 'known', 'must', 'me', 'none', 'f', 'this', 'getting', 'anywhere', 'nine', 'can', 'theirs', 'following', 'my', 'example', 'indicated', "didn't", 'indicates', 'something', 'want', 'needs', 'rather', 'meanwhile', 'how', 'instead', 'okay', 'tried', 'may', 'after', 'different', 'hereupon', 'such', 'a', 'third', 'whenever', 'maybe', 'appreciate', 'q', 'ones', 'so', 'specifying', 'allow', 'keeps', "that's", 'six', 'help', "don't", 'indeed', 'over', 'mainly', 'soon', 'course', "won't", 'looks', 'still', 'its', 'before', 'thank', "he's", 'selves', 'inward', 'actually', 'better', 'whether', 'willing', 'thanx', 'ours', 'might', "haven't", 'then', 'non', 'someone', 'somebody', 'thereby', "you've", 'they', 'not', 'now', 'nor', 'several', 'hereafter', 'always', 'reasonably', 'whither', 'l', 'each', 'entirely', "isn't", 'mean', 'everyone', 'doing', 'eg', 'ex', 'our', 'beyond', 'out', 'them', 'hhhe', 'furthermore', 'since', 'looking', 're', 'seriously', "shouldn't", "they'll", 'got', 'cause', 'thereupon', "you're", 'given', 'like', 'que', 'besides', 'ask', 'anyhow', 'g', 'could', 'tries', 'keep', 'w', 'ltd', 'hence', 'onto', 'think', 'first', 'already', 'seeming', 'thereafter', 'one', 'done', 'another', 'awfully', "doesn't", 'little', 'their', 'accordingly', 'least', 'name', 'anyone', 'indicate', 'too', 'gives', 'mostly', 'behind', 'nobody', 'took', 'immediate', 'regards', 'somewhat', 'off', 'believe', 'herself', 'than', "here's", 'b', 'unfortunately', 'gotten', 'second', 'i', 'r', 'were', 'toward', 'are', 'and', 'beforehand', 'say', 'unlikely', 'have', 'need', 'seen', 'seem', 'saw', 'any', 'relatively', 'zero', 'thoroughly', 'latter', 'that', 'downwards', 'aside', 'thorough', 'also', 'take', 'which', 'exactly', 'unless', 'shall', 'who', "where's", 'most', 'eight', 'but', 'nothing', 'why', 'sub', 'especially', 'throughthhroughout', 'noone', 'later', 'm', 'yours', "you'll", 'definitely', 'normally', 'came', 'saying', 'particularly', 'anyway', 'fifth', 'outside', 'should', 'only', 'going', 'specify', 'do', 'his', 'above', 'get', 'between', 'overall', 'truly', "they'd", 'cannot', 'nearly', 'despite', 'during', 'him', 'regarding', 'qv', 'h', 'twice', 'she', 'contain', 'x', 'where', 'thanks', 'ignored', 'up', 'namely', 'anyways', 'best', 'wonder', 'said', 'away', 'currently', 'please', 'enough', "there's", 'various', 'hopefully', 'probably', 'neither', 'across', 'available', 'we', 'useful', 'however', 'come', 'both', 'c', 'last', 'many', "wouldn't", 'thence', 'according', 'against', 'etc', 's', 'became', 'com', "can't", 'otherwise', 'among', 'liked', 'co', 'afterwards', 'seems', 'whatever', 'alone', "couldn't", 'moreover', 'considering', 'sensible', 'described', "it's", 'three', 'been', 'whom', 'much', 'wherein', 'hardly', "it'd", 'wants', 'corresponding', 'latterly', 'concerning', 'else', 'hers', 'former', 'those', 'myself', 'novel', 'look', 'these', 'value', 'n', 'will', 'near', 'theres', 'seven', 'whereafter', 'almost', 'wherever', 'is', 'thus', 'it', 'cant', 'itself', 'in', 'ie', 'y', 'if', 'containing', 'perhaps', 'insofar', 'same', 'clearly', 'beside', 'when', 'gets', "weren't", 'used', 'see', 'somewhere', 'upon', 'uses', 'kept', 'whereby', 'nevertheless', 'whole', 'well', 'anybody', 'obviously', 'without', 'comes', 'very', 'the', 'self', 'lest', 'just', 'less', 'being', 'able', 'presumably', 'greetings', 'regardless', 'yes', 'yet', 'unto', "we've", 'had', 'except', 'has', 'ought', "t's", 'around', "who's", 'possible', 'five', 'know', 'using', 'apart', 'necessary', 'd', 'follows', 'either', 'become', 'towards', 'therein', 'because', 'old', 'often', 'some', 'somehow', 'sure', 'specified', 'ourselves', 'happens', 'for', 'though', 'per', 'everything', 'does', 'provides', 'tends', 't', 'be', 'nowhere', 'although', 'by', 'on', 'about', 'ok', 'anything', 'oh', 'of', 'v', 'o', 'whence', 'plus', 'consequently', 'or', 'seeing', 'own', 'formerly', 'into', 'within', 'down', 'appropriate', 'right', "c's", 'your', 'her', 'there', 'inasmuch', 'inner', 'way', 'was', 'himself', 'elsewhere', "i've", 'becoming', 'amongst', 'hi', 'trying', 'with', 'he', "they're", "wasn't", 'wish', 'j', "hasn't", 'us', 'until', 'placed', 'below', 'un', 'z', "we'd", 'gone', 'sometimes', 'associated', 'certain', 'am', 'an', 'as', 'sometime', 'at', 'et', 'inc', 'again', 'uucp', 'no', 'whereas', 'nd', 'lately', 'other', 'you', 'really', "what's", 'welcome', "let's", 'serious', 'e', 'together', 'having', 'u', "we're", 'everywhere', 'hello', 'once'])