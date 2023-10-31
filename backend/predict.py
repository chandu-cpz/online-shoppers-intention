def predict(Administrative, ProductRelated, ProductRelated_Duration, 
            BounceRates, ExitRates, PageValues, Month, VisitorType):
    import sklearn
    import pickle
    import pandas as pd
    import json
    import warnings
    warnings.filterwarnings('ignore')
    print("Started Predicting....")

    try:
        with open("/home/chandu/git/online-shoppers-intention/rfc.pkl") as f:
            model = pickle.load(f)
        with open("/home/chandu/git/online-shoppers-intention/scaler.pkl", 'rb') as f:
            scaler = pickle.load(f)
    except:
        return "Failed to load PKL files"
     # Create input DataFrame
    input_df = pd.DataFrame([[Administrative, ProductRelated, ProductRelated_Duration,  
                           BounceRates, ExitRates, PageValues,Month,VisitorType]])
    
    input_df = scaler.transform(input_df)


    #Predict 
    pred = model.predict_proba(input_df)
    print(pred)

    result = {
        'prediction': pred.tolist()
    }
    print(result)
    result_json = json.dumps(result)
    
    return result_json