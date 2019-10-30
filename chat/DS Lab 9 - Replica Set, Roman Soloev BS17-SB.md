# DS Lab 9 - Replica Set, Roman Soloev BS17-SB

rs.status():
```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-30T08:09:02.578Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572422936, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-10-30T08:08:56.303Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572422936, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-30T08:08:56.303Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572422936, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572422936, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-10-30T08:08:56.303Z"),
		"lastDurableWallTime" : ISODate("2019-10-30T08:08:56.303Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572422916, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572422916, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-10-29T19:41:14.150Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572378064, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-29T19:41:15.073Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-29T19:41:15.993Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "node1:27017",
			"ip" : "172.31.37.158",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 45173,
			"optime" : {
				"ts" : Timestamp(1572422936, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-30T08:08:56Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572378074, 1),
			"electionDate" : ISODate("2019-10-29T19:41:14Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "node2:27017",
			"ip" : "172.31.30.121",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 44878,
			"optime" : {
				"ts" : Timestamp(1572422936, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572422936, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-30T08:08:56Z"),
			"optimeDurableDate" : ISODate("2019-10-30T08:08:56Z"),
			"lastHeartbeat" : ISODate("2019-10-30T08:09:01.451Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-30T08:09:01.451Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "node1:27017",
			"syncSourceHost" : "node1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "node3:27017",
			"ip" : "172.31.45.187",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 44878,
			"optime" : {
				"ts" : Timestamp(1572422936, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572422936, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-30T08:08:56Z"),
			"optimeDurableDate" : ISODate("2019-10-30T08:08:56Z"),
			"lastHeartbeat" : ISODate("2019-10-30T08:09:02.549Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-30T08:09:02.549Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "node1:27017",
			"syncSourceHost" : "node1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572422936, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572422936, 1)
}

```

rs.conf():
```
rs0:PRIMARY> rs.conf()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "node1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "node2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "node3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db895cf5219e021b6426486")
	}
}

```

chat:
![](https://i.imgur.com/Mz4OeR3.jpg)

## After shutting:

rs.status():
```
rs0:SECONDARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-30T08:19:29.984Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572423569, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-10-30T08:19:29.323Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572423569, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-30T08:19:29.323Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572423569, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572423569, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-10-30T08:19:29.323Z"),
		"lastDurableWallTime" : ISODate("2019-10-30T08:19:29.323Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572423519, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572423519, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-10-30T08:18:28.453Z"),
		"termAtElection" : NumberLong(2),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572423506, 1),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572423506, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 0,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-30T08:18:29.320Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-30T08:18:29.937Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "node1:27017",
			"ip" : "172.31.37.158",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-10-30T08:19:28.464Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-30T08:18:27.658Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "Couldn't get a connection within the time limit",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 1,
			"name" : "node2:27017",
			"ip" : "172.31.30.121",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 45510,
			"optime" : {
				"ts" : Timestamp(1572423569, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-30T08:19:29Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572423508, 1),
			"electionDate" : ISODate("2019-10-30T08:18:28Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "node3:27017",
			"ip" : "172.31.45.187",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 45505,
			"optime" : {
				"ts" : Timestamp(1572423559, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572423559, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-30T08:19:19Z"),
			"optimeDurableDate" : ISODate("2019-10-30T08:19:19Z"),
			"lastHeartbeat" : ISODate("2019-10-30T08:19:28.483Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-30T08:19:29.966Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "node2:27017",
			"syncSourceHost" : "node2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572423569, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572423569, 1)
}

```

rs.conf():
```
rs0:PRIMARY> rs.conf()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "node1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "node2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "node3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db895cf5219e021b6426486")
	}
}

```

chat:
![](https://i.imgur.com/9GfOWsF.jpg)


